# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class User(pulumi.CustomResource):
    """
    Manages a V1 DB user resource within OpenStack.
    """
    def __init__(__self__, __name__, __opts__=None, databases=None, host=None, instance_id=None, name=None, password=None, region=None):
        """Create a User resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['databases'] = databases

        __props__['host'] = host

        if not instance_id:
            raise TypeError('Missing required property instance_id')
        __props__['instance_id'] = instance_id

        __props__['name'] = name

        if not password:
            raise TypeError('Missing required property password')
        __props__['password'] = password

        if not region:
            raise TypeError('Missing required property region')
        __props__['region'] = region

        super(User, __self__).__init__(
            'openstack:database/user:User',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

