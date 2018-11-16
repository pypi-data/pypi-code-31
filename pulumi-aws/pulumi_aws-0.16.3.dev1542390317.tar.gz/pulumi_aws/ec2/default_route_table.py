# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class DefaultRouteTable(pulumi.CustomResource):
    """
    Provides a resource to manage a Default VPC Routing Table.
    
    Each VPC created in AWS comes with a Default Route Table that can be managed, but not
    destroyed. **This is an advanced resource**, and has special caveats to be aware
    of when using it. Please read this document in its entirety before using this
    resource. It is recommended you **do not** use both `aws_default_route_table` to
    manage the default route table **and** use the `aws_main_route_table_association`,
    due to possible conflict in routes.
    
    The `aws_default_route_table` behaves differently from normal resources, in that
    Terraform does not _create_ this resource, but instead attempts to "adopt" it
    into management. We can do this because each VPC created has a Default Route
    Table that cannot be destroyed, and is created with a single route.
    
    When Terraform first adopts the Default Route Table, it **immediately removes all
    defined routes**. It then proceeds to create any routes specified in the
    configuration. This step is required so that only the routes specified in the
    configuration present in the Default Route Table.
    
    For more information about Route Tables, see the AWS Documentation on
    [Route Tables][aws-route-tables].
    
    For more information about managing normal Route Tables in Terraform, see our
    documentation on [aws_route_table][tf-route-tables].
    
    ~> **NOTE on Route Tables and Routes:** Terraform currently
    provides both a standalone Route resource and a Route Table resource with routes
    defined in-line. At this time you cannot use a Route Table with in-line routes
    in conjunction with any Route resources. Doing so will cause
    a conflict of rule settings and will overwrite routes.
    
    """
    def __init__(__self__, __name__, __opts__=None, default_route_table_id=None, propagating_vgws=None, routes=None, tags=None):
        """Create a DefaultRouteTable resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not default_route_table_id:
            raise TypeError('Missing required property default_route_table_id')
        __props__['default_route_table_id'] = default_route_table_id

        __props__['propagating_vgws'] = propagating_vgws

        __props__['routes'] = routes

        __props__['tags'] = tags

        __props__['vpc_id'] = None

        super(DefaultRouteTable, __self__).__init__(
            'aws:ec2/defaultRouteTable:DefaultRouteTable',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

