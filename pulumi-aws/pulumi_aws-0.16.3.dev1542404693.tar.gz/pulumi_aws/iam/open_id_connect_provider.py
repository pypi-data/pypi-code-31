# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class OpenIdConnectProvider(pulumi.CustomResource):
    """
    Provides an IAM OpenID Connect provider.
    """
    def __init__(__self__, __name__, __opts__=None, client_id_lists=None, thumbprint_lists=None, url=None):
        """Create a OpenIdConnectProvider resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not client_id_lists:
            raise TypeError('Missing required property client_id_lists')
        __props__['client_id_lists'] = client_id_lists

        if not thumbprint_lists:
            raise TypeError('Missing required property thumbprint_lists')
        __props__['thumbprint_lists'] = thumbprint_lists

        if not url:
            raise TypeError('Missing required property url')
        __props__['url'] = url

        __props__['arn'] = None

        super(OpenIdConnectProvider, __self__).__init__(
            'aws:iam/openIdConnectProvider:OpenIdConnectProvider',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

