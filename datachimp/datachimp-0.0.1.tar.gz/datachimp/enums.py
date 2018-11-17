class ClientEvent(object):
    AUTH = 1
    MODEL_PARAM = 2
    EVAL_PARAM = 3
    DURATION_PARAM = 4
    EXPERIMENT_START = 5
    EXPERIMENT_END = 6
    CODE_FILE = 7
    COMPLETED = 10
    GET_EXPERIMENT_METRIC_FILTER = 8
    GET_EXPERIMENT_METRIC_DATA = 9
    GET_EXPERIMENT_DURATION_FILTER = 11
    GET_EXPERIMENT_DURATION_DATA = 12
    HEART_BEAT = 13
    DATASET_ID = 14

class ExperimentStatus(object):
    IN_PROCESS = 1
    COMPLETED = 2
