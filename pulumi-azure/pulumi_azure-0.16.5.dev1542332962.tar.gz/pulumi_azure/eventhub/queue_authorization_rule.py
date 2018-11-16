# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class QueueAuthorizationRule(pulumi.CustomResource):
    """
    Manages an Authorization Rule for a ServiceBus Queue.
    """
    def __init__(__self__, __name__, __opts__=None, listen=None, manage=None, name=None, namespace_name=None, queue_name=None, resource_group_name=None, send=None):
        """Create a QueueAuthorizationRule resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['listen'] = listen

        __props__['manage'] = manage

        __props__['name'] = name

        if not namespace_name:
            raise TypeError('Missing required property namespace_name')
        __props__['namespace_name'] = namespace_name

        if not queue_name:
            raise TypeError('Missing required property queue_name')
        __props__['queue_name'] = queue_name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        __props__['resource_group_name'] = resource_group_name

        __props__['send'] = send

        __props__['primary_connection_string'] = None
        __props__['primary_key'] = None
        __props__['secondary_connection_string'] = None
        __props__['secondary_key'] = None

        super(QueueAuthorizationRule, __self__).__init__(
            'azure:eventhub/queueAuthorizationRule:QueueAuthorizationRule',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

