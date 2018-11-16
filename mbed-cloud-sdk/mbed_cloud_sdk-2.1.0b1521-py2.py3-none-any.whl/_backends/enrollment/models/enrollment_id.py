# coding: utf-8

"""
    Enrollment API

    Connect Enrollment Service allows users to claim the ownership of a device which is not yet assigned to an account. A device without an assigned account can be a device purchased from the open market (OEM dealer) or a device transferred from an account to another. More information in [Device ownership: First-to-claim](/docs/current/connecting/device-ownership-first-to-claim-by-enrollment-list.html) document. 

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EnrollmentId(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enrollment_identity': 'str'
    }

    attribute_map = {
        'enrollment_identity': 'enrollment_identity'
    }

    def __init__(self, enrollment_identity=None):
        """
        EnrollmentId - a model defined in Swagger
        """

        self._enrollment_identity = enrollment_identity
        self.discriminator = None

    @property
    def enrollment_identity(self):
        """
        Gets the enrollment_identity of this EnrollmentId.
        Enrollment identity.

        :return: The enrollment_identity of this EnrollmentId.
        :rtype: str
        """
        return self._enrollment_identity

    @enrollment_identity.setter
    def enrollment_identity(self, enrollment_identity):
        """
        Sets the enrollment_identity of this EnrollmentId.
        Enrollment identity.

        :param enrollment_identity: The enrollment_identity of this EnrollmentId.
        :type: str
        """
        if enrollment_identity is None:
            raise ValueError("Invalid value for `enrollment_identity`, must not be `None`")
        if enrollment_identity is not None and not re.search('^A-[A-Za-z0-9:]{95}$', enrollment_identity):
            raise ValueError("Invalid value for `enrollment_identity`, must be a follow pattern or equal to `/^A-[A-Za-z0-9:]{95}$/`")

        self._enrollment_identity = enrollment_identity

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, EnrollmentId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
