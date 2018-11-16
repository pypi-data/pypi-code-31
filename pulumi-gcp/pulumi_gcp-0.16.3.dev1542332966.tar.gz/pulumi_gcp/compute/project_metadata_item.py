# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class ProjectMetadataItem(pulumi.CustomResource):
    """
    Manages a single key/value pair on metadata common to all instances for
    a project in GCE. Using `google_compute_project_metadata_item` lets you
    manage a single key/value setting in Terraform rather than the entire
    project metadata map.
    """
    def __init__(__self__, __name__, __opts__=None, key=None, project=None, value=None):
        """Create a ProjectMetadataItem resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not key:
            raise TypeError('Missing required property key')
        __props__['key'] = key

        __props__['project'] = project

        if not value:
            raise TypeError('Missing required property value')
        __props__['value'] = value

        super(ProjectMetadataItem, __self__).__init__(
            'gcp:compute/projectMetadataItem:ProjectMetadataItem',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

