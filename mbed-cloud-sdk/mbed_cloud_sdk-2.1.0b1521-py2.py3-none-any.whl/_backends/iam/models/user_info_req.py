# coding: utf-8

"""
    Account Management API

    API for managing accounts, users, creating API keys, uploading trusted certificates

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserInfoReq(object):
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
        'address': 'str',
        'email': 'str',
        'full_name': 'str',
        'groups': 'list[str]',
        'is_gtc_accepted': 'bool',
        'is_marketing_accepted': 'bool',
        'password': 'str',
        'phone_number': 'str',
        'username': 'str'
    }

    attribute_map = {
        'address': 'address',
        'email': 'email',
        'full_name': 'full_name',
        'groups': 'groups',
        'is_gtc_accepted': 'is_gtc_accepted',
        'is_marketing_accepted': 'is_marketing_accepted',
        'password': 'password',
        'phone_number': 'phone_number',
        'username': 'username'
    }

    def __init__(self, address=None, email=None, full_name=None, groups=None, is_gtc_accepted=None, is_marketing_accepted=None, password=None, phone_number=None, username=None):
        """
        UserInfoReq - a model defined in Swagger
        """

        self._address = address
        self._email = email
        self._full_name = full_name
        self._groups = groups
        self._is_gtc_accepted = is_gtc_accepted
        self._is_marketing_accepted = is_marketing_accepted
        self._password = password
        self._phone_number = phone_number
        self._username = username
        self.discriminator = None

    @property
    def address(self):
        """
        Gets the address of this UserInfoReq.
        Address, not longer than 100 characters.

        :return: The address of this UserInfoReq.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this UserInfoReq.
        Address, not longer than 100 characters.

        :param address: The address of this UserInfoReq.
        :type: str
        """

        self._address = address

    @property
    def email(self):
        """
        Gets the email of this UserInfoReq.
        The email address, not longer than 254 characters.

        :return: The email of this UserInfoReq.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserInfoReq.
        The email address, not longer than 254 characters.

        :param email: The email of this UserInfoReq.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def full_name(self):
        """
        Gets the full_name of this UserInfoReq.
        The full name of the user, not longer than 100 characters.

        :return: The full_name of this UserInfoReq.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """
        Sets the full_name of this UserInfoReq.
        The full name of the user, not longer than 100 characters.

        :param full_name: The full_name of this UserInfoReq.
        :type: str
        """

        self._full_name = full_name

    @property
    def groups(self):
        """
        Gets the groups of this UserInfoReq.
        A list of IDs of the groups this user belongs to.

        :return: The groups of this UserInfoReq.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this UserInfoReq.
        A list of IDs of the groups this user belongs to.

        :param groups: The groups of this UserInfoReq.
        :type: list[str]
        """

        self._groups = groups

    @property
    def is_gtc_accepted(self):
        """
        Gets the is_gtc_accepted of this UserInfoReq.
        A flag indicating that the General Terms and Conditions has been accepted.

        :return: The is_gtc_accepted of this UserInfoReq.
        :rtype: bool
        """
        return self._is_gtc_accepted

    @is_gtc_accepted.setter
    def is_gtc_accepted(self, is_gtc_accepted):
        """
        Sets the is_gtc_accepted of this UserInfoReq.
        A flag indicating that the General Terms and Conditions has been accepted.

        :param is_gtc_accepted: The is_gtc_accepted of this UserInfoReq.
        :type: bool
        """

        self._is_gtc_accepted = is_gtc_accepted

    @property
    def is_marketing_accepted(self):
        """
        Gets the is_marketing_accepted of this UserInfoReq.
        A flag indicating that receiving marketing information has been accepted.

        :return: The is_marketing_accepted of this UserInfoReq.
        :rtype: bool
        """
        return self._is_marketing_accepted

    @is_marketing_accepted.setter
    def is_marketing_accepted(self, is_marketing_accepted):
        """
        Sets the is_marketing_accepted of this UserInfoReq.
        A flag indicating that receiving marketing information has been accepted.

        :param is_marketing_accepted: The is_marketing_accepted of this UserInfoReq.
        :type: bool
        """

        self._is_marketing_accepted = is_marketing_accepted

    @property
    def password(self):
        """
        Gets the password of this UserInfoReq.
        The password when creating a new user. It will be generated when not present in the request.

        :return: The password of this UserInfoReq.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UserInfoReq.
        The password when creating a new user. It will be generated when not present in the request.

        :param password: The password of this UserInfoReq.
        :type: str
        """

        self._password = password

    @property
    def phone_number(self):
        """
        Gets the phone_number of this UserInfoReq.
        Phone number, not longer than 100 characters.

        :return: The phone_number of this UserInfoReq.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this UserInfoReq.
        Phone number, not longer than 100 characters.

        :param phone_number: The phone_number of this UserInfoReq.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def username(self):
        """
        Gets the username of this UserInfoReq.
        A username containing alphanumerical letters and -,._@+= characters. It must be at least 4 but not more than 30 character long.

        :return: The username of this UserInfoReq.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UserInfoReq.
        A username containing alphanumerical letters and -,._@+= characters. It must be at least 4 but not more than 30 character long.

        :param username: The username of this UserInfoReq.
        :type: str
        """

        self._username = username

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
        if not isinstance(other, UserInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
