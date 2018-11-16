# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Cluster(pulumi.CustomResource):
    """
    Manages a V1 Magnum cluster resource within OpenStack.
    """
    def __init__(__self__, __name__, __opts__=None, cluster_template_id=None, create_timeout=None, discovery_url=None, docker_volume_size=None, flavor=None, keypair=None, labels=None, master_count=None, master_flavor=None, name=None, node_count=None, region=None):
        """Create a Cluster resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not cluster_template_id:
            raise TypeError('Missing required property cluster_template_id')
        __props__['cluster_template_id'] = cluster_template_id

        __props__['create_timeout'] = create_timeout

        __props__['discovery_url'] = discovery_url

        __props__['docker_volume_size'] = docker_volume_size

        __props__['flavor'] = flavor

        __props__['keypair'] = keypair

        __props__['labels'] = labels

        __props__['master_count'] = master_count

        __props__['master_flavor'] = master_flavor

        __props__['name'] = name

        __props__['node_count'] = node_count

        __props__['region'] = region

        __props__['api_address'] = None
        __props__['coe_version'] = None
        __props__['container_version'] = None
        __props__['created_at'] = None
        __props__['master_addresses'] = None
        __props__['node_addresses'] = None
        __props__['project_id'] = None
        __props__['stack_id'] = None
        __props__['updated_at'] = None
        __props__['user_id'] = None

        super(Cluster, __self__).__init__(
            'openstack:containerinfra/cluster:Cluster',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

