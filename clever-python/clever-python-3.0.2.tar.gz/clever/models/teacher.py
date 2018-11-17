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


class Teacher(object):
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
        'created': 'str',
        'credentials': 'Credentials',
        'district': 'str',
        'email': 'str',
        'id': 'str',
        'last_modified': 'str',
        'name': 'Name',
        'school': 'str',
        'schools': 'list[str]',
        'sis_id': 'str',
        'state_id': 'str',
        'teacher_number': 'str',
        'title': 'str'
    }

    attribute_map = {
        'created': 'created',
        'credentials': 'credentials',
        'district': 'district',
        'email': 'email',
        'id': 'id',
        'last_modified': 'last_modified',
        'name': 'name',
        'school': 'school',
        'schools': 'schools',
        'sis_id': 'sis_id',
        'state_id': 'state_id',
        'teacher_number': 'teacher_number',
        'title': 'title'
    }

    def __init__(self, created=None, credentials=None, district=None, email=None, id=None, last_modified=None, name=None, school=None, schools=None, sis_id=None, state_id=None, teacher_number=None, title=None):
        """
        Teacher - a model defined in Swagger
        """

        self._created = None
        self._credentials = None
        self._district = None
        self._email = None
        self._id = None
        self._last_modified = None
        self._name = None
        self._school = None
        self._schools = None
        self._sis_id = None
        self._state_id = None
        self._teacher_number = None
        self._title = None
        self.discriminator = None

        if created is not None:
          self.created = created
        if credentials is not None:
          self.credentials = credentials
        if district is not None:
          self.district = district
        if email is not None:
          self.email = email
        if id is not None:
          self.id = id
        if last_modified is not None:
          self.last_modified = last_modified
        if name is not None:
          self.name = name
        if school is not None:
          self.school = school
        if schools is not None:
          self.schools = schools
        if sis_id is not None:
          self.sis_id = sis_id
        if state_id is not None:
          self.state_id = state_id
        if teacher_number is not None:
          self.teacher_number = teacher_number
        if title is not None:
          self.title = title

    @property
    def created(self):
        """
        Gets the created of this Teacher.

        :return: The created of this Teacher.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Teacher.

        :param created: The created of this Teacher.
        :type: str
        """

        self._created = created

    @property
    def credentials(self):
        """
        Gets the credentials of this Teacher.

        :return: The credentials of this Teacher.
        :rtype: Credentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this Teacher.

        :param credentials: The credentials of this Teacher.
        :type: Credentials
        """

        self._credentials = credentials

    @property
    def district(self):
        """
        Gets the district of this Teacher.

        :return: The district of this Teacher.
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """
        Sets the district of this Teacher.

        :param district: The district of this Teacher.
        :type: str
        """

        self._district = district

    @property
    def email(self):
        """
        Gets the email of this Teacher.

        :return: The email of this Teacher.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Teacher.

        :param email: The email of this Teacher.
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """
        Gets the id of this Teacher.

        :return: The id of this Teacher.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Teacher.

        :param id: The id of this Teacher.
        :type: str
        """

        self._id = id

    @property
    def last_modified(self):
        """
        Gets the last_modified of this Teacher.

        :return: The last_modified of this Teacher.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """
        Sets the last_modified of this Teacher.

        :param last_modified: The last_modified of this Teacher.
        :type: str
        """

        self._last_modified = last_modified

    @property
    def name(self):
        """
        Gets the name of this Teacher.

        :return: The name of this Teacher.
        :rtype: Name
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Teacher.

        :param name: The name of this Teacher.
        :type: Name
        """

        self._name = name

    @property
    def school(self):
        """
        Gets the school of this Teacher.

        :return: The school of this Teacher.
        :rtype: str
        """
        return self._school

    @school.setter
    def school(self, school):
        """
        Sets the school of this Teacher.

        :param school: The school of this Teacher.
        :type: str
        """

        self._school = school

    @property
    def schools(self):
        """
        Gets the schools of this Teacher.

        :return: The schools of this Teacher.
        :rtype: list[str]
        """
        return self._schools

    @schools.setter
    def schools(self, schools):
        """
        Sets the schools of this Teacher.

        :param schools: The schools of this Teacher.
        :type: list[str]
        """

        self._schools = schools

    @property
    def sis_id(self):
        """
        Gets the sis_id of this Teacher.

        :return: The sis_id of this Teacher.
        :rtype: str
        """
        return self._sis_id

    @sis_id.setter
    def sis_id(self, sis_id):
        """
        Sets the sis_id of this Teacher.

        :param sis_id: The sis_id of this Teacher.
        :type: str
        """

        self._sis_id = sis_id

    @property
    def state_id(self):
        """
        Gets the state_id of this Teacher.

        :return: The state_id of this Teacher.
        :rtype: str
        """
        return self._state_id

    @state_id.setter
    def state_id(self, state_id):
        """
        Sets the state_id of this Teacher.

        :param state_id: The state_id of this Teacher.
        :type: str
        """

        self._state_id = state_id

    @property
    def teacher_number(self):
        """
        Gets the teacher_number of this Teacher.

        :return: The teacher_number of this Teacher.
        :rtype: str
        """
        return self._teacher_number

    @teacher_number.setter
    def teacher_number(self, teacher_number):
        """
        Sets the teacher_number of this Teacher.

        :param teacher_number: The teacher_number of this Teacher.
        :type: str
        """

        self._teacher_number = teacher_number

    @property
    def title(self):
        """
        Gets the title of this Teacher.

        :return: The title of this Teacher.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Teacher.

        :param title: The title of this Teacher.
        :type: str
        """

        self._title = title

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
        if not isinstance(other, Teacher):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
