# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Topic(pulumi.CustomResource):
    """
    Provides an SNS topic resource
    """
    def __init__(__self__, __name__, __opts__=None, application_failure_feedback_role_arn=None, application_success_feedback_role_arn=None, application_success_feedback_sample_rate=None, delivery_policy=None, display_name=None, http_failure_feedback_role_arn=None, http_success_feedback_role_arn=None, http_success_feedback_sample_rate=None, lambda_failure_feedback_role_arn=None, lambda_success_feedback_role_arn=None, lambda_success_feedback_sample_rate=None, name=None, name_prefix=None, policy=None, sqs_failure_feedback_role_arn=None, sqs_success_feedback_role_arn=None, sqs_success_feedback_sample_rate=None):
        """Create a Topic resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['application_failure_feedback_role_arn'] = application_failure_feedback_role_arn

        __props__['application_success_feedback_role_arn'] = application_success_feedback_role_arn

        __props__['application_success_feedback_sample_rate'] = application_success_feedback_sample_rate

        __props__['delivery_policy'] = delivery_policy

        __props__['display_name'] = display_name

        __props__['http_failure_feedback_role_arn'] = http_failure_feedback_role_arn

        __props__['http_success_feedback_role_arn'] = http_success_feedback_role_arn

        __props__['http_success_feedback_sample_rate'] = http_success_feedback_sample_rate

        __props__['lambda_failure_feedback_role_arn'] = lambda_failure_feedback_role_arn

        __props__['lambda_success_feedback_role_arn'] = lambda_success_feedback_role_arn

        __props__['lambda_success_feedback_sample_rate'] = lambda_success_feedback_sample_rate

        __props__['name'] = name

        __props__['name_prefix'] = name_prefix

        __props__['policy'] = policy

        __props__['sqs_failure_feedback_role_arn'] = sqs_failure_feedback_role_arn

        __props__['sqs_success_feedback_role_arn'] = sqs_success_feedback_role_arn

        __props__['sqs_success_feedback_sample_rate'] = sqs_success_feedback_sample_rate

        __props__['arn'] = None

        super(Topic, __self__).__init__(
            'aws:sns/topic:Topic',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

