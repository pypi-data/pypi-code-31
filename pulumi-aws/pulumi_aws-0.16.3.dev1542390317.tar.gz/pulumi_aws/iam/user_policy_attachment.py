# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class UserPolicyAttachment(pulumi.CustomResource):
    """
    Attaches a Managed IAM Policy to an IAM user
    
    """
    def __init__(__self__, __name__, __opts__=None, policy_arn=None, user=None):
        """Create a UserPolicyAttachment resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not policy_arn:
            raise TypeError('Missing required property policy_arn')
        __props__['policy_arn'] = policy_arn

        if not user:
            raise TypeError('Missing required property user')
        __props__['user'] = user

        super(UserPolicyAttachment, __self__).__init__(
            'aws:iam/userPolicyAttachment:UserPolicyAttachment',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

