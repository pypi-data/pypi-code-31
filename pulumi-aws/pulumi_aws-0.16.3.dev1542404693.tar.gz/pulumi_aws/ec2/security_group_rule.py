# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class SecurityGroupRule(pulumi.CustomResource):
    """
    Provides a security group rule resource. Represents a single `ingress` or
    `egress` group rule, which can be added to external Security Groups.
    
    ~> **NOTE on Security Groups and Security Group Rules:** Terraform currently
    provides both a standalone Security Group Rule resource (a single `ingress` or
    `egress` rule), and a Security Group resource with `ingress` and `egress` rules
    defined in-line. At this time you cannot use a Security Group with in-line rules
    in conjunction with any Security Group Rule resources. Doing so will cause
    a conflict of rule settings and will overwrite rules.
    
    ~> **NOTE:** Setting `protocol = "all"` or `protocol = -1` with `from_port` and `to_port` will result in the EC2 API creating a security group rule with all ports open. This API behavior cannot be controlled by Terraform and may generate warnings in the future.
    """
    def __init__(__self__, __name__, __opts__=None, cidr_blocks=None, description=None, from_port=None, ipv6_cidr_blocks=None, prefix_list_ids=None, protocol=None, security_group_id=None, self=None, source_security_group_id=None, to_port=None, type=None):
        """Create a SecurityGroupRule resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['cidr_blocks'] = cidr_blocks

        __props__['description'] = description

        if not from_port:
            raise TypeError('Missing required property from_port')
        __props__['from_port'] = from_port

        __props__['ipv6_cidr_blocks'] = ipv6_cidr_blocks

        __props__['prefix_list_ids'] = prefix_list_ids

        if not protocol:
            raise TypeError('Missing required property protocol')
        __props__['protocol'] = protocol

        if not security_group_id:
            raise TypeError('Missing required property security_group_id')
        __props__['security_group_id'] = security_group_id

        __props__['self'] = self

        __props__['source_security_group_id'] = source_security_group_id

        if not to_port:
            raise TypeError('Missing required property to_port')
        __props__['to_port'] = to_port

        if not type:
            raise TypeError('Missing required property type')
        __props__['type'] = type

        super(SecurityGroupRule, __self__).__init__(
            'aws:ec2/securityGroupRule:SecurityGroupRule',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

