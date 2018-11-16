# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class TargetGroupAttachment(pulumi.CustomResource):
    """
    Provides the ability to register instances and containers with an Application Load Balancer (ALB) or Network Load Balancer (NLB) target group. For attaching resources with Elastic Load Balancer (ELB), see the [`aws_elb_attachment` resource](https://www.terraform.io/docs/providers/aws/r/elb_attachment.html).
    
    ~> **Note:** `aws_alb_target_group_attachment` is known as `aws_lb_target_group_attachment`. The functionality is identical.
    """
    def __init__(__self__, __name__, __opts__=None, availability_zone=None, port=None, target_group_arn=None, target_id=None):
        """Create a TargetGroupAttachment resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['availability_zone'] = availability_zone

        __props__['port'] = port

        if not target_group_arn:
            raise TypeError('Missing required property target_group_arn')
        __props__['target_group_arn'] = target_group_arn

        if not target_id:
            raise TypeError('Missing required property target_id')
        __props__['target_id'] = target_id

        super(TargetGroupAttachment, __self__).__init__(
            'aws:elasticloadbalancingv2/targetGroupAttachment:TargetGroupAttachment',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

