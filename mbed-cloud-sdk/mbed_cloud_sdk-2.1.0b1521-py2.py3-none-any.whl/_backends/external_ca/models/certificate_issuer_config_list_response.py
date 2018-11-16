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


class CertificateIssuerConfigListResponse(object):
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
        'after': 'str',
        'data': 'list[CertificateIssuerConfigResponse]',
        'limit': 'int',
        'object': 'str',
        'order': 'str',
        'total_count': 'int'
    }

    attribute_map = {
        'after': 'after',
        'data': 'data',
        'limit': 'limit',
        'object': 'object',
        'order': 'order',
        'total_count': 'total_count'
    }

    def __init__(self, after=None, data=None, limit=None, object=None, order=None, total_count=None):
        """
        CertificateIssuerConfigListResponse - a model defined in Swagger
        """

        self._after = after
        self._data = data
        self._limit = limit
        self._object = object
        self._order = order
        self._total_count = total_count
        self.discriminator = None

    @property
    def after(self):
        """
        Gets the after of this CertificateIssuerConfigListResponse.
        The entity ID to fetch after current result set.

        :return: The after of this CertificateIssuerConfigListResponse.
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """
        Sets the after of this CertificateIssuerConfigListResponse.
        The entity ID to fetch after current result set.

        :param after: The after of this CertificateIssuerConfigListResponse.
        :type: str
        """

        self._after = after

    @property
    def data(self):
        """
        Gets the data of this CertificateIssuerConfigListResponse.
        List of certificate issuers.

        :return: The data of this CertificateIssuerConfigListResponse.
        :rtype: list[CertificateIssuerConfigResponse]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this CertificateIssuerConfigListResponse.
        List of certificate issuers.

        :param data: The data of this CertificateIssuerConfigListResponse.
        :type: list[CertificateIssuerConfigResponse]
        """

        self._data = data

    @property
    def limit(self):
        """
        Gets the limit of this CertificateIssuerConfigListResponse.
        The number of results returned.

        :return: The limit of this CertificateIssuerConfigListResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this CertificateIssuerConfigListResponse.
        The number of results returned.

        :param limit: The limit of this CertificateIssuerConfigListResponse.
        :type: int
        """

        self._limit = limit

    @property
    def object(self):
        """
        Gets the object of this CertificateIssuerConfigListResponse.
        Describes the type of objects in the list.

        :return: The object of this CertificateIssuerConfigListResponse.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this CertificateIssuerConfigListResponse.
        Describes the type of objects in the list.

        :param object: The object of this CertificateIssuerConfigListResponse.
        :type: str
        """
        allowed_values = ["list"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def order(self):
        """
        Gets the order of this CertificateIssuerConfigListResponse.
        The order of results.

        :return: The order of this CertificateIssuerConfigListResponse.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this CertificateIssuerConfigListResponse.
        The order of results.

        :param order: The order of this CertificateIssuerConfigListResponse.
        :type: str
        """
        allowed_values = ["ASC", "DESC"]
        if order not in allowed_values:
            raise ValueError(
                "Invalid value for `order` ({0}), must be one of {1}"
                .format(order, allowed_values)
            )

        self._order = order

    @property
    def total_count(self):
        """
        Gets the total_count of this CertificateIssuerConfigListResponse.
        The total number or records.

        :return: The total_count of this CertificateIssuerConfigListResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this CertificateIssuerConfigListResponse.
        The total number or records.

        :param total_count: The total_count of this CertificateIssuerConfigListResponse.
        :type: int
        """

        self._total_count = total_count

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
        if not isinstance(other, CertificateIssuerConfigListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
