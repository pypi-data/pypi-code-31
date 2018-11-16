# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Alias(pulumi.CustomResource):
    """
    Creates a Lambda function alias. Creates an alias that points to the specified Lambda function version.
    
    For information about Lambda and how to use it, see [What is AWS Lambda?][1]
    For information about function aliases, see [CreateAlias][2] and [AliasRoutingConfiguration][3] in the API docs.
    """
    def __init__(__self__, __name__, __opts__=None, description=None, function_name=None, function_version=None, name=None, routing_config=None):
        """Create a Alias resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['description'] = description

        if not function_name:
            raise TypeError('Missing required property function_name')
        __props__['function_name'] = function_name

        if not function_version:
            raise TypeError('Missing required property function_version')
        __props__['function_version'] = function_version

        __props__['name'] = name

        __props__['routing_config'] = routing_config

        __props__['arn'] = None

        super(Alias, __self__).__init__(
            'aws:lambda/alias:Alias',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

