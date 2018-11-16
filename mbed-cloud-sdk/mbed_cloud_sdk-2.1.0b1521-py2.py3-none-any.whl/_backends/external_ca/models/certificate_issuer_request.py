# coding: utf-8

"""
    Third party CA management API

    API for managing third party CA for creating certificates on Pelion Device Management

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CertificateIssuerRequest(object):
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
        'description': 'str',
        'issuer_attributes': 'dict(str, str)',
        'issuer_credentials': 'dict(str, str)',
        'issuer_type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'issuer_attributes': 'issuer_attributes',
        'issuer_credentials': 'issuer_credentials',
        'issuer_type': 'issuer_type',
        'name': 'name'
    }

    def __init__(self, description=None, issuer_attributes=None, issuer_credentials=None, issuer_type=None, name=None):
        """
        CertificateIssuerRequest - a model defined in Swagger
        """

        self._description = description
        self._issuer_attributes = issuer_attributes
        self._issuer_credentials = issuer_credentials
        self._issuer_type = issuer_type
        self._name = name
        self.discriminator = None

    @property
    def description(self):
        """
        Gets the description of this CertificateIssuerRequest.
        General description for the certificate issuer.

        :return: The description of this CertificateIssuerRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CertificateIssuerRequest.
        General description for the certificate issuer.

        :param description: The description of this CertificateIssuerRequest.
        :type: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")

        self._description = description

    @property
    def issuer_attributes(self):
        """
        Gets the issuer_attributes of this CertificateIssuerRequest.
        General attributes for connecting the certificate issuer. When the issuer_type is GLOBAL_SIGN, the value shall be empty. When the issuer_type is CFSSL_AUTH, see definition of CfsslAttributes. 

        :return: The issuer_attributes of this CertificateIssuerRequest.
        :rtype: dict(str, str)
        """
        return self._issuer_attributes

    @issuer_attributes.setter
    def issuer_attributes(self, issuer_attributes):
        """
        Sets the issuer_attributes of this CertificateIssuerRequest.
        General attributes for connecting the certificate issuer. When the issuer_type is GLOBAL_SIGN, the value shall be empty. When the issuer_type is CFSSL_AUTH, see definition of CfsslAttributes. 

        :param issuer_attributes: The issuer_attributes of this CertificateIssuerRequest.
        :type: dict(str, str)
        """

        self._issuer_attributes = issuer_attributes

    @property
    def issuer_credentials(self):
        """
        Gets the issuer_credentials of this CertificateIssuerRequest.
        The credentials required for connecting to the certificate issuer. When the issuer_type is GLOBAL_SIGN, see definition of GlobalSignCredentials. When the issuer_type is CFSSL_AUTH, see definition of CfsslAuthCredentials. 

        :return: The issuer_credentials of this CertificateIssuerRequest.
        :rtype: dict(str, str)
        """
        return self._issuer_credentials

    @issuer_credentials.setter
    def issuer_credentials(self, issuer_credentials):
        """
        Sets the issuer_credentials of this CertificateIssuerRequest.
        The credentials required for connecting to the certificate issuer. When the issuer_type is GLOBAL_SIGN, see definition of GlobalSignCredentials. When the issuer_type is CFSSL_AUTH, see definition of CfsslAuthCredentials. 

        :param issuer_credentials: The issuer_credentials of this CertificateIssuerRequest.
        :type: dict(str, str)
        """

        self._issuer_credentials = issuer_credentials

    @property
    def issuer_type(self):
        """
        Gets the issuer_type of this CertificateIssuerRequest.
        The type of the certificate issuer. - GLOBAL_SIGN:   Certificates are issued by GlobalSign service. The users must provide their own GlobalSign account credentials. - CFSSL_AUTH:   Certificates are issued by CFSSL authenticated signing service.   The users must provide their own CFSSL host_url and credentials. 

        :return: The issuer_type of this CertificateIssuerRequest.
        :rtype: str
        """
        return self._issuer_type

    @issuer_type.setter
    def issuer_type(self, issuer_type):
        """
        Sets the issuer_type of this CertificateIssuerRequest.
        The type of the certificate issuer. - GLOBAL_SIGN:   Certificates are issued by GlobalSign service. The users must provide their own GlobalSign account credentials. - CFSSL_AUTH:   Certificates are issued by CFSSL authenticated signing service.   The users must provide their own CFSSL host_url and credentials. 

        :param issuer_type: The issuer_type of this CertificateIssuerRequest.
        :type: str
        """
        if issuer_type is None:
            raise ValueError("Invalid value for `issuer_type`, must not be `None`")
        allowed_values = ["GLOBAL_SIGN", "CFSSL_AUTH"]
        if issuer_type not in allowed_values:
            raise ValueError(
                "Invalid value for `issuer_type` ({0}), must be one of {1}"
                .format(issuer_type, allowed_values)
            )

        self._issuer_type = issuer_type

    @property
    def name(self):
        """
        Gets the name of this CertificateIssuerRequest.
        Certificate issuer name, unique per account.

        :return: The name of this CertificateIssuerRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CertificateIssuerRequest.
        Certificate issuer name, unique per account.

        :param name: The name of this CertificateIssuerRequest.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")

        self._name = name

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
        if not isinstance(other, CertificateIssuerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
