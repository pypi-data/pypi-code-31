from ibm_ai_openscale.base_classes.instances import AIInstance
from ibm_ai_openscale.utils import *
from .consts import WMLConsts


class WatsonMachineLearningInstance(AIInstance):
    """
    Describes Watson Machine Learning instance.

    :param service_credentials: credentials of WML instance
    :type service_credentials: dict
    """
    def __init__(self, service_credentials):
        validate_type(service_credentials, 'service_credentials', dict, True)
        validate_type(service_credentials['instance_id'], 'service_credentials.instance_id', str, True)
        validate_type(service_credentials['url'], 'service_credentials.url', str, True)
        validate_type(service_credentials['apikey'], 'service_credentials.apikey', str, True)
        validate_type(service_credentials['username'], 'service_credentials.username', str, True)
        validate_type(service_credentials['password'], 'service_credentials.password', str, True)
        AIInstance.__init__(self, service_credentials['instance_id'], service_credentials, WMLConsts.SERVICE_TYPE)