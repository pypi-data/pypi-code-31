import pulumi
import pulumi.runtime

from ... import tables

class Status(pulumi.CustomResource):
    """
    Status is a return value for calls that don't return other objects.
    """
    def __init__(self, __name__, __opts__=None, code=None, details=None, message=None, metadata=None, reason=None, status=None):
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'v1'
        __props__['kind'] = 'Status'
        __props__['code'] = code
        __props__['details'] = details
        __props__['message'] = message
        __props__['metadata'] = metadata
        __props__['reason'] = reason
        __props__['status'] = status

        super(Status, self).__init__(
            "kubernetes:core/v1:Status",
            __name__,
            __props__,
            __opts__)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
