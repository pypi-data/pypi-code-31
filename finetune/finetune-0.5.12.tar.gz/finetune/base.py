import os
import random
import weakref
import atexit
import warnings
import itertools
import math
from abc import ABCMeta, abstractmethod
from copy import deepcopy
import tempfile
import time
import shutil
import glob
from contextlib import contextmanager
import pathlib

import tqdm
import numpy as np
import tensorflow as tf
from tensorflow.data import Dataset
from sklearn.model_selection import train_test_split
from tensorflow.train import SessionRunHook

from finetune.utils import interpolate_pos_embed, list_transpose
from finetune.encoding import EncodedOutput
from finetune.input_pipeline import ENCODER
from finetune.config import get_default_config
from finetune.saver import Saver
from finetune.errors import FinetuneError
from finetune.model import get_model_fn, PredictMode
from finetune.download import download_data_if_required
from finetune.estimator_utils import PatchedParameterServerStrategy

JL_BASE = os.path.join(os.path.dirname(__file__), "model", "Base_model.jl")


class BaseModel(object, metaclass=ABCMeta):
    """
    A sklearn-style task agnostic base class for finetuning a Transformer language model.
    """

    def __init__(self, config=None, **kwargs):
        """ 
        For a full list of configuration options, see `finetune.config`.
        
        :param config: A config object generated by `finetune.config.get_config` or None (for default config).
        :param **kwargs: key-value pairs of config items to override.
        """
        weak_self = weakref.ref(self)

        def cleanup():
            strong_self = weak_self()
            if strong_self is not None:
                BaseModel.__del__(strong_self)

        atexit.register(cleanup)

        self.config = config or get_default_config()
        self.config.update(kwargs)

        if self.config.num_layers_trained != self.config.n_layer and self.config.train_embeddings:
            raise ValueError("If you are only finetuning a subset of the layers, you cannot finetune embeddings.")

        self.input_pipeline = self._get_input_pipeline()
        download_data_if_required()
        self._initialize()

    @abstractmethod
    def _get_input_pipeline(self):
        pass

    def _initialize(self):
        # Initializes the non-serialized bits of the class.
        self._set_random_seed(self.config.seed)

        # state for prediction caching
        self._predictions = None
        self._cached_predict = False
        self._closed = False

        if self.config.tensorboard_folder is not None:
            self.estimator_dir = os.path.abspath(
                os.path.join(self.config.tensorboard_folder, str(int(time.time())))
            )
            pathlib.Path(self.estimator_dir).mkdir(parents=True, exist_ok=True)
            self.cleanup_glob = None
        else:
            self.estimator_dir = tempfile.mkdtemp(prefix="Finetune")
            self.cleanup_glob = self.estimator_dir

        def process_embeddings(name, value):
            if "/we:0" not in name:
                return value

            vocab_size = ENCODER.vocab_size
            word_embeddings = value[:vocab_size - len(ENCODER.special_tokens)]
            special_embed = value[len(word_embeddings): vocab_size]
            positional_embed = value[vocab_size:]
            if self.config.interpolate_pos_embed and self.config.max_length != len(positional_embed):
                positional_embed = interpolate_pos_embed(positional_embed, self.config.max_length)
            elif self.config.max_length > len(positional_embed):
                raise ValueError("Max Length cannot be greater than {} if interploate_pos_embed is turned off".format(
                    len(positional_embed)))
            else:
                positional_embed = positional_embed[:self.config.max_length]

            embeddings = np.concatenate((word_embeddings, special_embed, positional_embed), axis=0)
            return embeddings

        base_model_path = os.path.join(os.path.dirname(__file__), "model", self.config.base_model_path)
        self.saver = Saver(
            fallback_filename=base_model_path,
            exclude_matches=None if self.config.save_adam_vars else "Adam",
            variable_transforms=[process_embeddings],
            save_dtype=self.config.save_dtype
        )

    @abstractmethod
    def _predict_op(self, logits, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def _predict_proba_op(self, logits, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def _target_model(self, *, featurizer_state, targets, n_outputs, train=False, reuse=None, **kwargs):
        # Overridden by subclass to attach a target model onto the shared base featurizer.
        raise NotImplementedError

    def _n_steps(self, n_examples, batch_size, n_gpus):
        steps = int(math.ceil(
            n_examples / (batch_size * n_gpus)
        ))
        return steps

    def finetune(self, Xs, Y=None, batch_size=None):
        if not callable(Xs) and Y is not None and len(Xs) != len(Y):
            raise FinetuneError(
                "Mismatch between number of examples ({}) and number of targets ({}) provided.".format(
                    len(Xs),
                    len(Y)
                )
            )
        batch_size = batch_size or self.config.batch_size

        val_input_fn, train_input_fn, val_size, val_interval = self.input_pipeline.get_train_input_fns(Xs, Y, batch_size=batch_size)
        if val_size <= 10 and self.config.keep_best_model:
            tf.logging.warning(
                "Early stopping / keeping best model with a validation size of {} is likely to case undesired results".format(val_size))

        steps_per_epoch = self._n_steps(
            n_examples=self.config.dataset_size,
            batch_size=batch_size, 
            n_gpus=max(1, len(self.config.visible_gpus))
        )
        num_steps = steps_per_epoch * self.config.n_epochs
        estimator = self.get_estimator()
        train_hooks = [
            self.saver.get_saver_hook(
                estimator=estimator,
                keep_best_model=self.config.keep_best_model,
                steps_per_epoch=steps_per_epoch,
                early_stopping_steps=self.config.early_stopping_steps,
                eval_frequency=val_interval
            ),
            
        ]
        if val_size > 0:
            train_hooks.append(
                tf.contrib.estimator.InMemoryEvaluatorHook(
                    estimator, val_input_fn, every_n_iter=val_interval, steps=val_size // batch_size
                )
            )
        
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            estimator.train(train_input_fn, hooks=train_hooks, steps=num_steps)

    def get_estimator(self, force_build_lm=False):
        conf = tf.ConfigProto(
            allow_soft_placement=self.config.soft_device_placement,
            log_device_placement=self.config.log_device_placement,
        )
        num_gpus = len(self.config.visible_gpus)
        if num_gpus > 1:
            distribute_strategy = PatchedParameterServerStrategy(num_gpus_per_worker=num_gpus)
        else:
            distribute_strategy = None

        config = tf.estimator.RunConfig(
            tf_random_seed=self.config.seed,
            save_summary_steps=self.config.val_interval,
            save_checkpoints_secs=None,
            save_checkpoints_steps=None,
            # disable auto summaries
            session_config=conf,
            log_step_count_steps=100,
            train_distribute=distribute_strategy,
            keep_checkpoint_max=1
        )

        model_fn = get_model_fn(
            target_model_fn=self._target_model,
            predict_op=self._predict_op,
            predict_proba_op=self._predict_proba_op,
            build_target_model=self.input_pipeline.target_dim is not None,
            build_lm=force_build_lm or self.config.lm_loss_coef > 0.0 or self.input_pipeline.target_dim is None,
            encoder=ENCODER,
            target_dim=self.input_pipeline.target_dim,
            label_encoder=self.input_pipeline.label_encoder,
            saver=self.saver
        )
        return tf.estimator.Estimator(
            model_dir=self.estimator_dir,
            model_fn=model_fn,
            config=config,
            params=self.config
        )

    def close(self):
        self._closed = True
        
        if self._predictions is not None:
            
            # force input fn termination
            try:
                for _ in self._predictions:
                    pass
            except AttributeError:
                pass

            self._predictions = None

    def _data_generator(self):
        self._cached_example = None
        while not self._closed:
            try:
                self._cached_example = self._data.pop(0)
                yield self._cached_example
            except IndexError:
                yield self._cached_example

    @contextmanager
    def cached_predict(self):
        """
        Context manager that prevents the recreation of the tensorflow graph on every call to BaseModel.predict().        
        """
        self._cached_predict = True
        yield self
        self._cached_predict = False
        self.close()

    def _cached_inference(self, Xs, mode=None):
        """
        Ensure graph is not rebuilt on subsequent calls to .predict()
        """
        self._data = Xs
        self._closed = False
        n = len(self._data)
        if self._predictions is None:
            _estimator = self.get_estimator()
            input_fn = self.input_pipeline.get_predict_input_fn(self._data_generator)
            self._predictions = _estimator.predict(input_fn=input_fn, predict_keys=mode)

        predictions = [None] * n
        for i in tqdm.tqdm(range(n), total=n, desc="Inference"):
            y = next(self._predictions)
            y = y[mode] if mode else y
            predictions[i] = y
        return predictions

    def _inference(self, Xs, mode=None):
        Xs = self.input_pipeline._format_for_inference(Xs)
        if self._cached_predict:
            return self._cached_inference(Xs=Xs, mode=mode)
        else:
            estimator = self.get_estimator()
            input_fn = self.input_pipeline.get_predict_input_fn(Xs)
            length = len(Xs) if not callable(Xs) else None

            predictions = tqdm.tqdm(
                estimator.predict(
                    input_fn=input_fn, predict_keys=mode
                ),
                total=length,
                desc="Inference"
            )
            return [pred[mode] if mode else pred for pred in predictions]
        
    def fit(self, *args, **kwargs):
        """ An alias for finetune. """
        return self.finetune(*args, **kwargs)

    def _predict(self, Xs):
        raw_preds = self._inference(Xs, PredictMode.NORMAL)
        return self.input_pipeline.label_encoder.inverse_transform(np.asarray(raw_preds))

    def predict(self, Xs):
        return self._predict(Xs)

    def _predict_proba(self, Xs):
        """
        Produce raw numeric outputs for proba predictions
        """
        raw_preds = self._inference(Xs, PredictMode.PROBAS)
        return raw_preds

    def predict_proba(self, *args, **kwargs):
        """
        The base method for predicting from the model.
        """
        raw_probas = self._predict_proba(*args, **kwargs)
        classes = self.input_pipeline.label_encoder.classes_

        formatted_predictions = []
        for probas in raw_probas:
            formatted_predictions.append(
                dict(zip(classes, probas))
            )
        return formatted_predictions

    def _featurize(self, Xs):
        raw_preds = self._inference(Xs, PredictMode.FEATURIZE)
        return np.asarray(raw_preds)

    @abstractmethod
    def featurize(self, *args, **kwargs):
        """
        Base method to get raw features out of the model.
        These features are the same that are fed into the target_model.
        """
        return self._featurize(*args, **kwargs)

    @classmethod
    def get_eval_fn(cls):
        raise NotImplementedError("No default eval function is given, please pass an explicit eval fn to grid_search")

    def transform(self, *args, **kwargs):
        """
        An alias for `featurize`.
        """
        return self.featurize(*args, **kwargs)

    def _set_random_seed(self, seed=None):
        seed = seed or self.config.seed
        random.seed(seed)
        np.random.seed(seed)
        tf.set_random_seed(seed)

    def generate_text(self, seed_text='', max_length=None, use_extra_toks=True):
        """
        Performs a prediction on the Language modeling objective given some seed text. It uses a noisy greedy decoding.
        Temperature parameter for decoding is set in the config.
        :param max_length: The maximum length to decode to.
        :param seed_text: Defaults to the empty string. This will form the starting point to begin modelling
        :return: A string containing the generated text.
        """
        def dataset_encoded():
            while not dataset_encoded.finished:
                yield {"tokens": arr_encoded.token_ids, "mask": arr_encoded.mask}

        dataset_encoded.finished = False

        def get_input_fn():
            types, shapes = self.input_pipeline.feed_shape_type_def()
            tf_dataset = Dataset.from_generator(dataset_encoded, types[0], shapes[0])
            return tf_dataset.batch(1)

        self.config.use_extra_toks = use_extra_toks
        encoded = ENCODER._encode([seed_text])
        if encoded == [] and not use_extra_toks:
            raise ValueError("If you are not using the extra tokens, you must provide some non-empty seed text")
        start = [ENCODER.start] if use_extra_toks else []
        encoded = EncodedOutput(token_ids=start + encoded.token_ids[0])

        estimator = self.get_estimator(force_build_lm=True)
        predict = estimator.predict(input_fn=get_input_fn,)

        EOS = ENCODER.clf_token
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")
            for i in range(len(encoded.token_ids) - 1, (max_length or self.config.max_length) - 2):
                arr_encoded = self.input_pipeline._array_format(encoded)
                class_idx = next(predict)[PredictMode.GENERATE_TEXT]
                encoded.token_ids.append(class_idx[i])
                if encoded.token_ids[-1] == EOS:
                    break
            dataset_encoded.finished = True

        del self.config["use_extra_toks"]

        return ENCODER.decode(encoded.token_ids)

    def __getstate__(self):
        """
        Leave serialization of all tf objects to tf
        """
        required_fields = [
            '_load_from_file', 'config', 'input_pipeline'
        ]
        serialized_state = {
            k: v for k, v in self.__dict__.items()
            if k in required_fields
        }
        return serialized_state

    def save(self, path):
        """
        Saves the state of the model to disk to the folder specific by `path`.  If `path` does not exist, it will be auto-created.

        Save is performed in two steps:
            - Serialize tf graph to disk using tf.Saver
            - Serialize python model using pickle

        Note:
            Does not serialize state of Adam optimizer.
            Should not be used to save / restore a training model.
        """
        if path is None:
            return

        path = os.path.abspath(path)
        self.saver.save(self, path)

    @classmethod
    def load(cls, path):
        """
        Load a saved fine-tuned model from disk.  Path provided should be a folder which contains .pkl and tf.Saver() files

        :param path: string path name to load model from.  Same value as previously provided to :meth:`save`. Must be a folder.
        """
        saver = Saver(JL_BASE)
        model = saver.load(path)
        model._initialize()
        model.saver.variables = saver.variables
        return model

    @classmethod
    def finetune_grid_search(cls, Xs, Y, *, test_size, config=None, eval_fn=None, probs=False, return_all=False):
        """
        Performs grid search over config items defined using "GridSearchable" objects and returns either full results or
        the config object that relates to the best results. The default config contains grid searchable objects for the
        most important parameters to search over.

        :param Xs: Input text. Either [num_samples] or [sequence, num_samples] for single or multi input models respectively.
        :param Y: Targets, A list of targets, [num_samples] that correspond to each sample in Xs.
        :param test_size: Int or float. If an int is given this number of samples is used to validate, if a float is
         given then that fraction of samples is used.
        :param config: A config object, or None to use the default config.
        :param eval_fn: An eval function that takes 2 inputs (prediction, truth) and returns a float, with a max value being desired.
        :param probs: If true, eval_fn is passed probability outputs from predict_proba, otherwise the output of predict is used.
        :param return_all: If True, all results are returned, if False, only the best config is returned.
        :return: default is to return the best config object. If return_all is true, it returns a list of tuples of the
            form [(config, eval_fn output), ... ]
        """
        if isinstance(Xs[0], str):
            Xs = [Xs]
        config = config or get_default_config()
        config.val_size = 0.0
        eval_fn = eval_fn or cls.get_eval_fn()

        trainXs, testXs, trainY, testY = train_test_split(list_transpose(Xs), Y, test_size=test_size, shuffle=True)
        trainXs = list_transpose(trainXs)
        testXs = list_transpose(testXs)
        gs = config.get_grid_searchable()
        ranged_keys = gs.keys()
        ranged_iterators = gs.values()
        grid_gen = itertools.product(*ranged_iterators)
        results = []
        for grid_item in grid_gen:
            config_ = deepcopy(config)
            config_.update(dict(zip(ranged_keys, grid_item)))
            instance = cls(config=config_)
            instance.finetune(*trainXs, Y=trainY)
            if probs:
                res = instance.predict_proba(*testXs)
            else:
                res = instance.predict(*testXs)
            results.append((config_, eval_fn(res, testY)))
            del instance

        if return_all:
            return results
        return max(results, key=lambda x: x[1])[0]

    @classmethod
    def finetune_grid_search_cv(cls, Xs, Y, *, n_splits, test_size, config=None, eval_fn=None, probs=False,
                                return_all=False):
        """
        Performs cross validated grid search over config items defined using "GridSearchable" objects and returns either full results or
        the config object that relates to the best results. The default config contains grid searchable objects for the
        most important parameters to search over.

        It should be noted that the cv splits are not guaranteed unique, but each split is given to each set of hparams.

        :param Xs: Input text. Either [num_samples] or [sequence, num_samples] for single or multi input models respectively.
        :param Y: Targets, A list of targets, [num_samples] that correspond to each sample in Xs.
        :param n_splits: Number of CV splits to do.
        :param test_size: Int or float. If an int is given this number of samples is used to validate, if a float is
            given then that fraction of samples is used.
        :param config: A config object, or None to use the default config.
        :param eval_fn: An eval function that takes 2 batches of outputs and returns a float, with a max value being
            desired. An arithmetic mean must make sense for this metric.
        :param probs: If true, eval_fn is passed probability outputs from predict_proba, otherwise the output of predict is used.
        :param return_all: If True, all results are returned, if False, only the best config is returned.
        :return: default is to return the best config object. If return_all is true, it returns a list of tuples of the
            form [(config, eval_fn output), ... ]
        """
        results = []
        for _ in range(n_splits):
            res = cls.finetune_grid_search(Xs, Y, test_size=test_size, probs=probs, eval_fn=eval_fn, config=config,
                                           return_all=True)
            results.append(res)
        results = list(zip(*results))
        aggregated_results = []
        for configuration in results:
            config_common = None
            sum_res = 0
            n_res = 0
            for config, result in configuration:
                config_common = config_common or config
                assert config == config_common
                n_res += 1
                sum_res += result
            aggregated_results.append((config_common, sum_res / n_res))

        if return_all:
            return aggregated_results

        return max(aggregated_results, key=lambda x: x[1])[0]

    def __del__(self):
        if hasattr(self, 'cleanup_glob') and self.cleanup_glob is not None:
            for file_or_folder in glob.glob(self.cleanup_glob):
                try:
                    shutil.rmtree(file_or_folder)
                except NotADirectoryError:
                    os.remove(file_or_folder)
