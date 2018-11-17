# coding: utf-8

"""
    Clever API

    The Clever API

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class District(object):
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
        'error': 'str',
        'id': 'str',
        'last_sync': 'str',
        'launch_date': 'str',
        'mdr_number': 'str',
        'name': 'str',
        'nces_id': 'str',
        'pause_end': 'str',
        'pause_start': 'str',
        'sis_type': 'str',
        'state': 'str'
    }

    attribute_map = {
        'error': 'error',
        'id': 'id',
        'last_sync': 'last_sync',
        'launch_date': 'launch_date',
        'mdr_number': 'mdr_number',
        'name': 'name',
        'nces_id': 'nces_id',
        'pause_end': 'pause_end',
        'pause_start': 'pause_start',
        'sis_type': 'sis_type',
        'state': 'state'
    }

    def __init__(self, error=None, id=None, last_sync=None, launch_date=None, mdr_number=None, name=None, nces_id=None, pause_end=None, pause_start=None, sis_type=None, state=None):
        """
        District - a model defined in Swagger
        """

        self._error = None
        self._id = None
        self._last_sync = None
        self._launch_date = None
        self._mdr_number = None
        self._name = None
        self._nces_id = None
        self._pause_end = None
        self._pause_start = None
        self._sis_type = None
        self._state = None
        self.discriminator = None

        if error is not None:
          self.error = error
        if id is not None:
          self.id = id
        if last_sync is not None:
          self.last_sync = last_sync
        if launch_date is not None:
          self.launch_date = launch_date
        if mdr_number is not None:
          self.mdr_number = mdr_number
        if name is not None:
          self.name = name
        if nces_id is not None:
          self.nces_id = nces_id
        if pause_end is not None:
          self.pause_end = pause_end
        if pause_start is not None:
          self.pause_start = pause_start
        if sis_type is not None:
          self.sis_type = sis_type
        if state is not None:
          self.state = state

    @property
    def error(self):
        """
        Gets the error of this District.

        :return: The error of this District.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this District.

        :param error: The error of this District.
        :type: str
        """

        self._error = error

    @property
    def id(self):
        """
        Gets the id of this District.

        :return: The id of this District.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this District.

        :param id: The id of this District.
        :type: str
        """

        self._id = id

    @property
    def last_sync(self):
        """
        Gets the last_sync of this District.

        :return: The last_sync of this District.
        :rtype: str
        """
        return self._last_sync

    @last_sync.setter
    def last_sync(self, last_sync):
        """
        Sets the last_sync of this District.

        :param last_sync: The last_sync of this District.
        :type: str
        """

        self._last_sync = last_sync

    @property
    def launch_date(self):
        """
        Gets the launch_date of this District.

        :return: The launch_date of this District.
        :rtype: str
        """
        return self._launch_date

    @launch_date.setter
    def launch_date(self, launch_date):
        """
        Sets the launch_date of this District.

        :param launch_date: The launch_date of this District.
        :type: str
        """

        self._launch_date = launch_date

    @property
    def mdr_number(self):
        """
        Gets the mdr_number of this District.

        :return: The mdr_number of this District.
        :rtype: str
        """
        return self._mdr_number

    @mdr_number.setter
    def mdr_number(self, mdr_number):
        """
        Sets the mdr_number of this District.

        :param mdr_number: The mdr_number of this District.
        :type: str
        """

        self._mdr_number = mdr_number

    @property
    def name(self):
        """
        Gets the name of this District.

        :return: The name of this District.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this District.

        :param name: The name of this District.
        :type: str
        """

        self._name = name

    @property
    def nces_id(self):
        """
        Gets the nces_id of this District.

        :return: The nces_id of this District.
        :rtype: str
        """
        return self._nces_id

    @nces_id.setter
    def nces_id(self, nces_id):
        """
        Sets the nces_id of this District.

        :param nces_id: The nces_id of this District.
        :type: str
        """

        self._nces_id = nces_id

    @property
    def pause_end(self):
        """
        Gets the pause_end of this District.

        :return: The pause_end of this District.
        :rtype: str
        """
        return self._pause_end

    @pause_end.setter
    def pause_end(self, pause_end):
        """
        Sets the pause_end of this District.

        :param pause_end: The pause_end of this District.
        :type: str
        """

        self._pause_end = pause_end

    @property
    def pause_start(self):
        """
        Gets the pause_start of this District.

        :return: The pause_start of this District.
        :rtype: str
        """
        return self._pause_start

    @pause_start.setter
    def pause_start(self, pause_start):
        """
        Sets the pause_start of this District.

        :param pause_start: The pause_start of this District.
        :type: str
        """

        self._pause_start = pause_start

    @property
    def sis_type(self):
        """
        Gets the sis_type of this District.

        :return: The sis_type of this District.
        :rtype: str
        """
        return self._sis_type

    @sis_type.setter
    def sis_type(self, sis_type):
        """
        Sets the sis_type of this District.

        :param sis_type: The sis_type of this District.
        :type: str
        """

        self._sis_type = sis_type

    @property
    def state(self):
        """
        Gets the state of this District.

        :return: The state of this District.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this District.

        :param state: The state of this District.
        :type: str
        """
        allowed_values = ["running", "pending", "error", "paused"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

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
        if not isinstance(other, District):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
