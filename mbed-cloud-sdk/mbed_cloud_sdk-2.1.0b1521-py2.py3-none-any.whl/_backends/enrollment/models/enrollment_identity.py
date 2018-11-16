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


class EnrollmentIdentity(object):
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
        'account_id': 'str',
        'claimed_at': 'datetime',
        'created_at': 'datetime',
        'enrolled_device_id': 'str',
        'enrollment_identity': 'str',
        'etag': 'str',
        'expires_at': 'datetime',
        'id': 'str',
        'object': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'claimed_at': 'claimed_at',
        'created_at': 'created_at',
        'enrolled_device_id': 'enrolled_device_id',
        'enrollment_identity': 'enrollment_identity',
        'etag': 'etag',
        'expires_at': 'expires_at',
        'id': 'id',
        'object': 'object'
    }

    def __init__(self, account_id=None, claimed_at=None, created_at=None, enrolled_device_id=None, enrollment_identity=None, etag=None, expires_at=None, id=None, object=None):
        """
        EnrollmentIdentity - a model defined in Swagger
        """

        self._account_id = account_id
        self._claimed_at = claimed_at
        self._created_at = created_at
        self._enrolled_device_id = enrolled_device_id
        self._enrollment_identity = enrollment_identity
        self._etag = etag
        self._expires_at = expires_at
        self._id = id
        self._object = object
        self.discriminator = None

    @property
    def account_id(self):
        """
        Gets the account_id of this EnrollmentIdentity.
        ID

        :return: The account_id of this EnrollmentIdentity.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this EnrollmentIdentity.
        ID

        :param account_id: The account_id of this EnrollmentIdentity.
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")

        self._account_id = account_id

    @property
    def claimed_at(self):
        """
        Gets the claimed_at of this EnrollmentIdentity.
        The time of claiming the device to be assigned to the account.

        :return: The claimed_at of this EnrollmentIdentity.
        :rtype: datetime
        """
        return self._claimed_at

    @claimed_at.setter
    def claimed_at(self, claimed_at):
        """
        Sets the claimed_at of this EnrollmentIdentity.
        The time of claiming the device to be assigned to the account.

        :param claimed_at: The claimed_at of this EnrollmentIdentity.
        :type: datetime
        """
        if claimed_at is None:
            raise ValueError("Invalid value for `claimed_at`, must not be `None`")

        self._claimed_at = claimed_at

    @property
    def created_at(self):
        """
        Gets the created_at of this EnrollmentIdentity.
        The time of the enrollment identity creation.

        :return: The created_at of this EnrollmentIdentity.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this EnrollmentIdentity.
        The time of the enrollment identity creation.

        :param created_at: The created_at of this EnrollmentIdentity.
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def enrolled_device_id(self):
        """
        Gets the enrolled_device_id of this EnrollmentIdentity.
        The ID of the device in the Device Directory once it has been registered.

        :return: The enrolled_device_id of this EnrollmentIdentity.
        :rtype: str
        """
        return self._enrolled_device_id

    @enrolled_device_id.setter
    def enrolled_device_id(self, enrolled_device_id):
        """
        Sets the enrolled_device_id of this EnrollmentIdentity.
        The ID of the device in the Device Directory once it has been registered.

        :param enrolled_device_id: The enrolled_device_id of this EnrollmentIdentity.
        :type: str
        """
        if enrolled_device_id is None:
            raise ValueError("Invalid value for `enrolled_device_id`, must not be `None`")
        if enrolled_device_id is not None and not re.search('^[A-Za-z0-9]{32}', enrolled_device_id):
            raise ValueError("Invalid value for `enrolled_device_id`, must be a follow pattern or equal to `/^[A-Za-z0-9]{32}/`")

        self._enrolled_device_id = enrolled_device_id

    @property
    def enrollment_identity(self):
        """
        Gets the enrollment_identity of this EnrollmentIdentity.
        Enrollment identity.

        :return: The enrollment_identity of this EnrollmentIdentity.
        :rtype: str
        """
        return self._enrollment_identity

    @enrollment_identity.setter
    def enrollment_identity(self, enrollment_identity):
        """
        Sets the enrollment_identity of this EnrollmentIdentity.
        Enrollment identity.

        :param enrollment_identity: The enrollment_identity of this EnrollmentIdentity.
        :type: str
        """
        if enrollment_identity is None:
            raise ValueError("Invalid value for `enrollment_identity`, must not be `None`")
        if enrollment_identity is not None and not re.search('^A-[A-Za-z0-9:]{95}$', enrollment_identity):
            raise ValueError("Invalid value for `enrollment_identity`, must be a follow pattern or equal to `/^A-[A-Za-z0-9:]{95}$/`")

        self._enrollment_identity = enrollment_identity

    @property
    def etag(self):
        """
        Gets the etag of this EnrollmentIdentity.

        :return: The etag of this EnrollmentIdentity.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this EnrollmentIdentity.

        :param etag: The etag of this EnrollmentIdentity.
        :type: str
        """
        if etag is None:
            raise ValueError("Invalid value for `etag`, must not be `None`")
        if etag is not None and not re.search('[A-Za-z0-9]{1,256}', etag):
            raise ValueError("Invalid value for `etag`, must be a follow pattern or equal to `/[A-Za-z0-9]{1,256}/`")

        self._etag = etag

    @property
    def expires_at(self):
        """
        Gets the expires_at of this EnrollmentIdentity.
        The enrollment claim expiration time. If the device does not connect to Mbed Cloud before the expiration, the claim is removed without a separate notice

        :return: The expires_at of this EnrollmentIdentity.
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """
        Sets the expires_at of this EnrollmentIdentity.
        The enrollment claim expiration time. If the device does not connect to Mbed Cloud before the expiration, the claim is removed without a separate notice

        :param expires_at: The expires_at of this EnrollmentIdentity.
        :type: datetime
        """
        if expires_at is None:
            raise ValueError("Invalid value for `expires_at`, must not be `None`")

        self._expires_at = expires_at

    @property
    def id(self):
        """
        Gets the id of this EnrollmentIdentity.
        Enrollment identity.

        :return: The id of this EnrollmentIdentity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EnrollmentIdentity.
        Enrollment identity.

        :param id: The id of this EnrollmentIdentity.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        if id is not None and not re.search('^[A-Za-z0-9]{32}', id):
            raise ValueError("Invalid value for `id`, must be a follow pattern or equal to `/^[A-Za-z0-9]{32}/`")

        self._id = id

    @property
    def object(self):
        """
        Gets the object of this EnrollmentIdentity.

        :return: The object of this EnrollmentIdentity.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this EnrollmentIdentity.

        :param object: The object of this EnrollmentIdentity.
        :type: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")
        allowed_values = ["enrollment"]
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
        if not isinstance(other, EnrollmentIdentity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
