import itertools
import math
import warnings
import copy

import tensorflow as tf
import numpy as np

from finetune.base import BaseModel, PredictMode
from finetune.target_encoders import SequenceLabelingEncoder, SequenceMultiLabelingEncoder
from finetune.network_modules import sequence_labeler
from finetune.crf import sequence_decode
from finetune.utils import indico_to_finetune_sequence, finetune_to_indico_sequence
from finetune.input_pipeline import BasePipeline, ENCODER
from finetune.estimator_utils import ProgressHook


class SequencePipeline(BasePipeline):
    def __init__(self, config, multi_label):
        super(SequencePipeline, self).__init__(config)
        self.multi_label = multi_label

    def _post_data_initialization(self, Y):
        Y_ = list(itertools.chain.from_iterable(Y))
        super()._post_data_initialization(Y_)

    def text_to_tokens_mask(self, X, Y=None):
        pad_token = [self.config.pad_token] if self.multi_label else self.config.pad_token
        out_gen = self._text_to_ids(X, Y=Y, pad_token=pad_token)
        for out in out_gen:
            feats = {"tokens": out.token_ids, "mask": out.mask}
            if Y is None:
                yield feats
            else:
                yield feats, self.label_encoder.transform(out.labels)

    def _format_for_encoding(self, X):
        return [X]

    def _format_for_inference(self, X):
        return [[x] for x in X]

    def feed_shape_type_def(self):
        TS = tf.TensorShape
        target_shape = (
            [self.config.max_length, self.label_encoder.target_dim] 
            if self.multi_label else [self.config.max_length]
        )
        return (
            (
                {
                    "tokens": tf.int32,
                    "mask": tf.float32
                },
                tf.int32
            ), 
            (
                {
                    "tokens": TS([self.config.max_length, 2]), 
                    "mask": TS([self.config.max_length])
                }, 
                TS(target_shape)
            )
        )

    def _target_encoder(self):
        if self.multi_label:
            return SequenceMultiLabelingEncoder()
        return SequenceLabelingEncoder()


class SequenceLabeler(BaseModel):
    """ 
    Labels each token in a sequence as belonging to 1 of N token classes.
    
    :param config: A :py:class:`finetune.config.Settings` object or None (for default config).
    :param \**kwargs: key-value pairs of config items to override.
    """

    defaults = {
        "n_epochs": 5,
        "lr_warmup": 0.1,
        "low_memory_mode": True,
        "chunk_long_sequences": True
    }

    def __init__(self, config=None, **kwargs):
        """ 
        For a full list of configuration options, see `finetune.config`.
        
        :param config: A config object generated by `finetune.config.get_config` or None (for default config).
        :param n_epochs: defaults to `5`.
        :param lr_warmup: defaults to `0.1`,
        :param low_memory_mode: defaults to `True`,
        :param chunk_long_sequences: defaults to `True`
        :param **kwargs: key-value pairs of config items to override.
        """
        d = copy.deepcopy(SequenceLabeler.defaults)
        d.update(kwargs)
        super().__init__(config=config, **d)

    def _get_input_pipeline(self):
        return SequencePipeline(config=self.config, multi_label=self.config.multi_label_sequences)

    def _initialize(self):
        self.multi_label = self.config.multi_label_sequences
        return super()._initialize()

    def finetune(self, Xs, Y=None, batch_size=None):
        Xs, Y_new = indico_to_finetune_sequence(Xs, labels=Y, multi_label=self.multi_label, none_value="<PAD>")
        Y = Y_new if Y is not None else None
        return super().finetune(Xs, Y=Y, batch_size=batch_size)

    def predict(self, X):
        """
        Produces a list of most likely class labels as determined by the fine-tuned model.

        :param X: A list / array of text, shape [batch]
        :returns: list of class labels.
        """
        chunk_size = self.config.max_length - 2
        step_size = chunk_size // 3
        arr_encoded = list(itertools.chain.from_iterable(self.input_pipeline._text_to_ids([x]) for x in X))
        labels, batch_probas = [], []
        for pred in self._inference(X, mode=None):
            labels.append(self.input_pipeline.label_encoder.inverse_transform(pred[PredictMode.NORMAL]))
            batch_probas.append(pred[PredictMode.PROBAS])

        all_subseqs = []
        all_labels = []
        all_probs = []

        doc_idx = -1
        for chunk_idx, (label_seq, proba_seq) in enumerate(zip(labels, batch_probas)):

            position_seq = arr_encoded[chunk_idx].char_locs
            start_of_doc = arr_encoded[chunk_idx].token_ids[0][0] == ENCODER.start
            end_of_doc = (
                    chunk_idx + 1 >= len(arr_encoded) or
                    arr_encoded[chunk_idx + 1].token_ids[0][0] == ENCODER.start
            )
            """
            Chunk idx for prediction.  Dividers at `step_size` increments.
            [  1  |  1  |  2  |  3  |  3  ]
            """
            start, end = 0, None
            if start_of_doc:
                # if this is the first chunk in a document, start accumulating from scratch
                doc_subseqs = []
                doc_labels = []
                doc_probs = []
                doc_idx += 1
                start_of_token = 0
                if not end_of_doc:
                    end = step_size * 2
            else:
                if end_of_doc:
                    # predict on the rest of sequence
                    start = step_size
                else:
                    # predict only on middle third
                    start, end = step_size, step_size * 2
            
            label_seq = label_seq[start:end]
            position_seq = position_seq[start:end]
            proba_seq = proba_seq[start:end]

            for label, position, proba in zip(label_seq, position_seq, proba_seq):
                if position == -1:
                    # indicates padding / special tokens
                    continue

                # if there are no current subsequence
                # or the current subsequence has the wrong label
                if not doc_subseqs or label != doc_labels[-1]:
                    # start new subsequence
                    doc_subseqs.append(X[doc_idx][start_of_token:position])
                    doc_labels.append(label)
                    doc_probs.append([proba])
                else:
                    # continue appending to current subsequence
                    doc_subseqs[-1] += X[doc_idx][start_of_token:position]
                    doc_probs[-1].append(proba)

                start_of_token = position

            if end_of_doc:
                # last chunk in a document
                prob_dicts = []
                for prob_seq in doc_probs:
                    # format probabilities as dictionary
                    probs = np.mean(np.vstack(prob_seq), axis=0)
                    prob_dicts.append(dict(zip(self.input_pipeline.label_encoder.classes_, probs)))
                    if self.multi_label:
                        del prob_dicts[-1][self.config.pad_token]

                all_subseqs.append(doc_subseqs)
                all_labels.append(doc_labels)
                all_probs.append(prob_dicts)
        _, doc_annotations = finetune_to_indico_sequence(
            raw_texts=X,
            subseqs=all_subseqs,
            labels=all_labels,
            probs=all_probs,
            subtoken_predictions=self.config.subtoken_predictions
        )

        return doc_annotations

    def featurize(self, X):
        """
        Embeds inputs in learned feature space. Can be called before or after calling :meth:`finetune`.

        :param Xs: An iterable of lists or array of text, shape [batch, n_inputs, tokens]
        :returns: np.array of features of shape (n_examples, embedding_size).
        """
        return self._featurize(X)

    def predict_proba(self, X):
        """
        Produces a list of most likely class labels as determined by the fine-tuned model.

        :param X: A list / array of text, shape [batch]
        :returns: list of class labels.
        """
        return self.predict(X)

    def _target_model(self, featurizer_state, targets, n_outputs, train=False, reuse=None, **kwargs):
        return sequence_labeler(
            hidden=featurizer_state['sequence_features'],
            targets=targets,
            n_targets=n_outputs,
            pad_id=self.input_pipeline.pad_idx,
            config=self.config,
            train=train,
            multilabel=self.multi_label,
            reuse=reuse,
            **kwargs
        )

    def _predict_op(self, logits, **kwargs):
        trans_mats = kwargs.get("transition_matrix")
        if self.multi_label:
            logits = tf.unstack(logits, axis=-1)
            label_idxs = []
            label_probas = []
            for logits_i, trans_mat_i in zip(logits, trans_mats):
                idx, prob = sequence_decode(logits_i, trans_mat_i)
                label_idxs.append(idx)
                label_probas.append(prob[:, :, 1:])
            label_idxs = tf.stack(label_idxs, axis=-1)
            label_probas = tf.stack(label_probas, axis=-1)
        else:
            label_idxs, label_probas = sequence_decode(logits, trans_mats)
        return label_idxs, label_probas

    def _predict_proba_op(self, logits, **kwargs):
        return tf.no_op()
