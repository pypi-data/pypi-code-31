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


class CertificateIssuerInfo(object):
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
        'created_at': 'datetime',
        'description': 'str',
        'etag': 'str',
        'id': 'str',
        'issuer_attributes': 'dict(str, str)',
        'issuer_type': 'str',
        'name': 'str',
        'object': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'description': 'description',
        'etag': 'etag',
        'id': 'id',
        'issuer_attributes': 'issuer_attributes',
        'issuer_type': 'issuer_type',
        'name': 'name',
        'object': 'object'
    }

    def __init__(self, created_at=None, description=None, etag=None, id=None, issuer_attributes=None, issuer_type=None, name=None, object=None):
        """
        CertificateIssuerInfo - a model defined in Swagger
        """

        self._created_at = created_at
        self._description = description
        self._etag = etag
        self._id = id
        self._issuer_attributes = issuer_attributes
        self._issuer_type = issuer_type
        self._name = name
        self._object = object
        self.discriminator = None

    @property
    def created_at(self):
        """
        Gets the created_at of this CertificateIssuerInfo.
        Creation UTC time RFC3339.

        :return: The created_at of this CertificateIssuerInfo.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this CertificateIssuerInfo.
        Creation UTC time RFC3339.

        :param created_at: The created_at of this CertificateIssuerInfo.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def description(self):
        """
        Gets the description of this CertificateIssuerInfo.
        General description for the certificate issuer.

        :return: The description of this CertificateIssuerInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CertificateIssuerInfo.
        General description for the certificate issuer.

        :param description: The description of this CertificateIssuerInfo.
        :type: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")

        self._description = description

    @property
    def etag(self):
        """
        Gets the etag of this CertificateIssuerInfo.
        Entity instance signature.

        :return: The etag of this CertificateIssuerInfo.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this CertificateIssuerInfo.
        Entity instance signature.

        :param etag: The etag of this CertificateIssuerInfo.
        :type: str
        """

        self._etag = etag

    @property
    def id(self):
        """
        Gets the id of this CertificateIssuerInfo.
        The ID of the certificate issuer.

        :return: The id of this CertificateIssuerInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CertificateIssuerInfo.
        The ID of the certificate issuer.

        :param id: The id of this CertificateIssuerInfo.
        :type: str
        """

        self._id = id

    @property
    def issuer_attributes(self):
        """
        Gets the issuer_attributes of this CertificateIssuerInfo.
        General attributes for connecting the certificate issuer. When the issuer_type is GLOBAL_SIGN, the value shall be empty. When the issuer_type is CFSSL_AUTH, see definition of CfsslAttributes. 

        :return: The issuer_attributes of this CertificateIssuerInfo.
        :rtype: dict(str, str)
        """
        return self._issuer_attributes

    @issuer_attributes.setter
    def issuer_attributes(self, issuer_attributes):
        """
        Sets the issuer_attributes of this CertificateIssuerInfo.
        General attributes for connecting the certificate issuer. When the issuer_type is GLOBAL_SIGN, the value shall be empty. When the issuer_type is CFSSL_AUTH, see definition of CfsslAttributes. 

        :param issuer_attributes: The issuer_attributes of this CertificateIssuerInfo.
        :type: dict(str, str)
        """

        self._issuer_attributes = issuer_attributes

    @property
    def issuer_type(self):
        """
        Gets the issuer_type of this CertificateIssuerInfo.
        The type of the certificate issuer. - GLOBAL_SIGN:   Certificates are issued by GlobalSign service. The users must provide their own GlobalSign account credentials. - CFSSL_AUTH:   Certificates are issued by CFSSL authenticated signing service.   The users must provide their own CFSSL host_url and credentials. 

        :return: The issuer_type of this CertificateIssuerInfo.
        :rtype: str
        """
        return self._issuer_type

    @issuer_type.setter
    def issuer_type(self, issuer_type):
        """
        Sets the issuer_type of this CertificateIssuerInfo.
        The type of the certificate issuer. - GLOBAL_SIGN:   Certificates are issued by GlobalSign service. The users must provide their own GlobalSign account credentials. - CFSSL_AUTH:   Certificates are issued by CFSSL authenticated signing service.   The users must provide their own CFSSL host_url and credentials. 

        :param issuer_type: The issuer_type of this CertificateIssuerInfo.
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
        Gets the name of this CertificateIssuerInfo.
        Certificate issuer name, unique per account.

        :return: The name of this CertificateIssuerInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CertificateIssuerInfo.
        Certificate issuer name, unique per account.

        :param name: The name of this CertificateIssuerInfo.
        :type: str
        """
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")

        self._name = name

    @property
    def object(self):
        """
        Gets the object of this CertificateIssuerInfo.

        :return: The object of this CertificateIssuerInfo.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this CertificateIssuerInfo.

        :param object: The object of this CertificateIssuerInfo.
        :type: str
        """
        allowed_values = ["certificate-issuer"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

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
        if not isinstance(other, CertificateIssuerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
