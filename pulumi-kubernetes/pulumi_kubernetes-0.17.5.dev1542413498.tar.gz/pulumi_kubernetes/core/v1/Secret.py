import pulumi
import pulumi.runtime

from ... import tables

class Secret(pulumi.CustomResource):
    """
    Secret holds secret data of a certain type. The total bytes of the values in the Data field must
    be less than MaxSecretSize bytes.
    """
    def __init__(self, __name__, __opts__=None, data=None, metadata=None, string_data=None, type=None):
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'v1'
        __props__['kind'] = 'Secret'
        __props__['data'] = data
        __props__['metadata'] = metadata
        __props__['stringData'] = string_data
        __props__['type'] = type

        super(Secret, self).__init__(
            "kubernetes:core/v1:Secret",
            __name__,
            __props__,
            __opts__)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
