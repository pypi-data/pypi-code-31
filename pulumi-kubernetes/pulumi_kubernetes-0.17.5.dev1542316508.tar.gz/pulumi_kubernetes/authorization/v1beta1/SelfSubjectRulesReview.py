import pulumi
import pulumi.runtime

from ... import tables

class SelfSubjectRulesReview(pulumi.CustomResource):
    """
    SelfSubjectRulesReview enumerates the set of actions the current user can perform within a
    namespace. The returned list of actions may be incomplete depending on the server's
    authorization mode, and any errors experienced during the evaluation. SelfSubjectRulesReview
    should be used by UIs to show/hide actions, or to quickly let an end user reason about their
    permissions. It should NOT Be used by external systems to drive authorization decisions as this
    raises confused deputy, cache lifetime/revocation, and correctness concerns.
    SubjectAccessReview, and LocalAccessReview are the correct way to defer authorization decisions
    to the API server.
    """
    def __init__(self, __name__, __opts__=None, metadata=None, spec=None, status=None):
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'authorization.k8s.io/v1beta1'
        __props__['kind'] = 'SelfSubjectRulesReview'
        if not spec:
            raise TypeError('Missing required property spec')
        __props__['spec'] = spec
        __props__['metadata'] = metadata
        __props__['status'] = status

        super(SelfSubjectRulesReview, self).__init__(
            "kubernetes:authorization.k8s.io/v1beta1:SelfSubjectRulesReview",
            __name__,
            __props__,
            __opts__)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
