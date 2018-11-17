from mlp_utils import Versions
from mlp_utils import ExecutionModeKeys
from mlp_utils import ModeKeys
from mlp_utils import log
from mlp_utils import console_colors

class Model():
  '''
each model script should have a global variable `MODEL` set with an instance of this class. Refer to the methods for more details.
'''
  versions = None
  allow_delete_model_dir = False
  reset_steps = False
  summery = None
  def __init__(self, versions, allow_delete_model_dir=False, reset_steps=False):
    '''
version: a instance of Version, which will be used to obtain the versios of the model to execute.
allow_delete_model_dir: if true, the directory specified by `model_dir` passed to the `pre_execution_hook` will be cleared, essentially removing any saved information of the model. This can be used when the model training needs to be reset. 
reset_steps: if true, the number of steps that has elapsed will be ignored and number of steps will be calculated as if no training as occurred. if false, the steps will be calucated by deducting the value returned by `get_trained_step_count`. 
'''
    if isinstance(versions, Versions):
      self.versions = versions
    else:
      raise ValueError("versions should be an instance of `Versions` class, but recived: {0}".format(type(versions)))
    self.allow_delete_model_dir = allow_delete_model_dir
    self.reset_steps = reset_steps

    
  #TODO: Does the exec_mode have to be here?
  def pre_execution_hook(self, version, model_dir, exec_mode=ExecutionModeKeys.TEST):
    '''
Before execution, this method will be called to set the version obtained from `self.versions`. Also `model_dir` will provide the destination to save the model in as specified in the config file. The exec_mode will be passed, with on of the keys as specified in `ExecutionModeKeys`. This function can be used to define the model's hyperparameters based on the information of the version being executed duering an iteration. This method will be once called before `train_model` for each version. 
'''
    raise NotImplementedError
  
  def train_model(self, input_fn, steps):
    '''
This will be called when the model is entering the traning phase. Ideally, what needs to happen in this function is to use the `input_fn` and train the model for a given number of steps which will be passed through `steps`. The input_fn passed here will be the object returned by the `get_train_input` method of the dataloader. In addition, other functionalities can be included here as well, such as saving the model parameters during training, etc. Th return value of the method will be logged.
'''
    raise NotImplementedError

  def evaluate_model(self,input_fn, steps):
    '''
This will be called when the model is entering the testing phase following the training phase. Ideally, what needs to happen in this function is to use the input_fn to obtain the inputs and test the model for a given number of steps. The input function passed here will be the object returned by the `get_train_input` and `get_test_input` methods of the dataloader. In addition to that other functionalities can be included here as well, such as saving the model parameters, producing additional statistics etc. the return value of the method will be logged.
'''
    raise NotImplementedError

  def get_current_version(self):
    '''
This function should return a dict, which represents the current version.
'''
    raise NotImplementedError

  def get_trained_step_count(self):
    '''
This function must return either `None` or a positive integer. The is used to determine how many steps have been completed and assess the number of steps the training should take. This is delegated to the `Model` as the process of determining the number is library specific.
'''
    raise NotImplementedError
  def clean_model_dir(self, model_dir):
    '''
This function will be called when a model needs to be reset and the directory `model_dir` needs to be cleared as well.
'''
    raise NotImplementedError

  def add_to_summery(self, content):
    '''
This function can be used to set the summery of the model, which will be added to the output when the output is generated by the pipeline.
try to include the relevent information you would want to refer to when assessing the output.
'''
    if self.summery is None:
      self.summery = ""
    self.summery += "\t\t{0}\n".format(content)

  def log(self, message,log_to_file=False, **kargs):
    '''
    This Function can be used to log details from within the model
    '''
    log("{}Model- {}{}".format(console_colors.CYAN_FG,
                               console_colors.RESET,
                               message),
        log=log_to_file, **kargs)



class DataLoader():
  summery = None
  def __init__(self, **kargs):
    raise NotImplementedError
    
  #TODO: remove this method? as each version will be given it's own dataloader....
  #     def set_classes(self, use_all_classes, classes_count):
  #       '''
  # This function will be called before the execution of a specific verion of a model. This function can be used to modify the data provided by dataloader based in the needs of the version of the model being executed. 
  # '''
  #       raise NotImplementedError
  def get_train_input(self, mode= ModeKeys.TRAIN, **kargs):
    '''
    This function returns an object which will be passed to the `Model.train_model` when executing the training function of the model, the same function will be used to evaluate the model following training using `Model.evaluate_model` . The the object returned by this function would depend on the how the return function will be used in the model. (eg: for Tensorflow models the returnn value can be a function object, for pyTorch it can be a Dataset object. In both cases the output of this function will be providing the data used for training)
'''
    raise NotImplementedError

  def get_test_input(self, **kargs):
    '''
This function returns an object which will be used to evaluate the model following training using `Model.evaluate_model`. The the object returned by this function would depend on the how the return function will be used in the model. (eg: for Tensorflow models the returnn value can be a function object, for pyTorch it can be a Dataset object.  In both cases the output of this function will be providing the data used for evaluation)
'''
    raise NotImplementedError

  def get_dataloader_summery(self, **kargs):
    '''
This function will be called to log a summery of the dataloader when logging the results of a model
    '''
    raise NotImplementedError

  def get_train_sample_count(self):
    '''
returns the number of datapoints being used as the training dataset. This will be used to assess the number of epocs during training and evaluating.
'''
    raise NotImplementedError

  def get_test_sample_count(self):
    '''
returns the number of datapoints being used as the testing dataset. This will be used to assess the number of epocs during training and evaluating.
'''
    raise NotImplementedError

  def add_to_summery(self, content):
    '''
This function can be used to set the summery of the dataloader, which will be added to the output when the output is generated by the pipeline.
'''
    if self.summery is None:
      self.summery = ""
    self.summery += "\t\t{0}\n".format(content)
  def log(self, message,log_to_file=False, **kargs):
    '''
    This Function can be used to log details from within the dataloader
    '''
    log("{}Model- {}{}".format(console_colors.CYAN_FG,
                               console_colors.RESET,
                               message),
        log=log_to_file, **kargs)

    
