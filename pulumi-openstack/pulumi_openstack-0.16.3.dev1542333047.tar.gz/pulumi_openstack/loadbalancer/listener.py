# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Listener(pulumi.CustomResource):
    """
    Manages a V2 listener resource within OpenStack.
    """
    def __init__(__self__, __name__, __opts__=None, admin_state_up=None, connection_limit=None, default_pool_id=None, default_tls_container_ref=None, description=None, loadbalancer_id=None, name=None, protocol=None, protocol_port=None, region=None, sni_container_refs=None, tenant_id=None):
        """Create a Listener resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['admin_state_up'] = admin_state_up

        __props__['connection_limit'] = connection_limit

        __props__['default_pool_id'] = default_pool_id

        __props__['default_tls_container_ref'] = default_tls_container_ref

        __props__['description'] = description

        if not loadbalancer_id:
            raise TypeError('Missing required property loadbalancer_id')
        __props__['loadbalancer_id'] = loadbalancer_id

        __props__['name'] = name

        if not protocol:
            raise TypeError('Missing required property protocol')
        __props__['protocol'] = protocol

        if not protocol_port:
            raise TypeError('Missing required property protocol_port')
        __props__['protocol_port'] = protocol_port

        __props__['region'] = region

        __props__['sni_container_refs'] = sni_container_refs

        __props__['tenant_id'] = tenant_id

        super(Listener, __self__).__init__(
            'openstack:loadbalancer/listener:Listener',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

