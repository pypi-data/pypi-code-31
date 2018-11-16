# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Server(pulumi.CustomResource):
    """
    Manage a PostgreSQL Server.
    """
    def __init__(__self__, __name__, __opts__=None, administrator_login=None, administrator_login_password=None, location=None, name=None, resource_group_name=None, sku=None, ssl_enforcement=None, storage_profile=None, tags=None, version=None):
        """Create a Server resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not administrator_login:
            raise TypeError('Missing required property administrator_login')
        __props__['administrator_login'] = administrator_login

        if not administrator_login_password:
            raise TypeError('Missing required property administrator_login_password')
        __props__['administrator_login_password'] = administrator_login_password

        if not location:
            raise TypeError('Missing required property location')
        __props__['location'] = location

        __props__['name'] = name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        __props__['resource_group_name'] = resource_group_name

        if not sku:
            raise TypeError('Missing required property sku')
        __props__['sku'] = sku

        if not ssl_enforcement:
            raise TypeError('Missing required property ssl_enforcement')
        __props__['ssl_enforcement'] = ssl_enforcement

        if not storage_profile:
            raise TypeError('Missing required property storage_profile')
        __props__['storage_profile'] = storage_profile

        __props__['tags'] = tags

        if not version:
            raise TypeError('Missing required property version')
        __props__['version'] = version

        __props__['fqdn'] = None

        super(Server, __self__).__init__(
            'azure:postgresql/server:Server',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

