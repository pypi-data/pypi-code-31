# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class KeyVault(pulumi.CustomResource):
    """
    Manages a Key Vault.
    
    ~> **NOTE:** It's possible to define Key Vault Access Policies both within the `azurerm_key_vault` resource via the `access_policy` block and by using the `azurerm_key_vault_access_policy` resource. However it's not possible to use both methods to manage Access Policies within a KeyVault, since there'll be conflicts.
    """
    def __init__(__self__, __name__, __opts__=None, access_policies=None, enabled_for_deployment=None, enabled_for_disk_encryption=None, enabled_for_template_deployment=None, location=None, name=None, network_acls=None, resource_group_name=None, sku=None, tags=None, tenant_id=None):
        """Create a KeyVault resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['access_policies'] = access_policies

        __props__['enabled_for_deployment'] = enabled_for_deployment

        __props__['enabled_for_disk_encryption'] = enabled_for_disk_encryption

        __props__['enabled_for_template_deployment'] = enabled_for_template_deployment

        if not location:
            raise TypeError('Missing required property location')
        __props__['location'] = location

        __props__['name'] = name

        __props__['network_acls'] = network_acls

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        __props__['resource_group_name'] = resource_group_name

        if not sku:
            raise TypeError('Missing required property sku')
        __props__['sku'] = sku

        __props__['tags'] = tags

        if not tenant_id:
            raise TypeError('Missing required property tenant_id')
        __props__['tenant_id'] = tenant_id

        __props__['vault_uri'] = None

        super(KeyVault, __self__).__init__(
            'azure:keyvault/keyVault:KeyVault',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

