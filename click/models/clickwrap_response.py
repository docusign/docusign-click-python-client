# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ClickwrapResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'clickwrap_id': 'str',
        'clickwrap_name': 'str',
        'created_time': 'object',
        'display_settings': 'DisplaySettings',
        'documents': 'list[Document]',
        'last_modified': 'object',
        'last_modified_by': 'str',
        'owner_user_id': 'str',
        'require_reacceptance': 'bool',
        'scheduled_date': 'object',
        'scheduled_reacceptance': 'ClickwrapScheduledReacceptance',
        'status': 'str',
        'version_id': 'str',
        'version_number': 'int'
    }

    attribute_map = {
        'account_id': 'accountId',
        'clickwrap_id': 'clickwrapId',
        'clickwrap_name': 'clickwrapName',
        'created_time': 'createdTime',
        'display_settings': 'displaySettings',
        'documents': 'documents',
        'last_modified': 'lastModified',
        'last_modified_by': 'lastModifiedBy',
        'owner_user_id': 'ownerUserId',
        'require_reacceptance': 'requireReacceptance',
        'scheduled_date': 'scheduledDate',
        'scheduled_reacceptance': 'scheduledReacceptance',
        'status': 'status',
        'version_id': 'versionId',
        'version_number': 'versionNumber'
    }

    def __init__(self, account_id=None, clickwrap_id=None, clickwrap_name=None, created_time=None, display_settings=None, documents=None, last_modified=None, last_modified_by=None, owner_user_id=None, require_reacceptance=None, scheduled_date=None, scheduled_reacceptance=None, status=None, version_id=None, version_number=None):  # noqa: E501
        """ClickwrapResponse - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._clickwrap_id = None
        self._clickwrap_name = None
        self._created_time = None
        self._display_settings = None
        self._documents = None
        self._last_modified = None
        self._last_modified_by = None
        self._owner_user_id = None
        self._require_reacceptance = None
        self._scheduled_date = None
        self._scheduled_reacceptance = None
        self._status = None
        self._version_id = None
        self._version_number = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if clickwrap_id is not None:
            self.clickwrap_id = clickwrap_id
        if clickwrap_name is not None:
            self.clickwrap_name = clickwrap_name
        if created_time is not None:
            self.created_time = created_time
        if display_settings is not None:
            self.display_settings = display_settings
        if documents is not None:
            self.documents = documents
        if last_modified is not None:
            self.last_modified = last_modified
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if owner_user_id is not None:
            self.owner_user_id = owner_user_id
        if require_reacceptance is not None:
            self.require_reacceptance = require_reacceptance
        if scheduled_date is not None:
            self.scheduled_date = scheduled_date
        if scheduled_reacceptance is not None:
            self.scheduled_reacceptance = scheduled_reacceptance
        if status is not None:
            self.status = status
        if version_id is not None:
            self.version_id = version_id
        if version_number is not None:
            self.version_number = version_number

    @property
    def account_id(self):
        """Gets the account_id of this ClickwrapResponse.  # noqa: E501

          # noqa: E501

        :return: The account_id of this ClickwrapResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ClickwrapResponse.

          # noqa: E501

        :param account_id: The account_id of this ClickwrapResponse.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def clickwrap_id(self):
        """Gets the clickwrap_id of this ClickwrapResponse.  # noqa: E501

          # noqa: E501

        :return: The clickwrap_id of this ClickwrapResponse.  # noqa: E501
        :rtype: str
        """
        return self._clickwrap_id

    @clickwrap_id.setter
    def clickwrap_id(self, clickwrap_id):
        """Sets the clickwrap_id of this ClickwrapResponse.

          # noqa: E501

        :param clickwrap_id: The clickwrap_id of this ClickwrapResponse.  # noqa: E501
        :type: str
        """

        self._clickwrap_id = clickwrap_id

    @property
    def clickwrap_name(self):
        """Gets the clickwrap_name of this ClickwrapResponse.  # noqa: E501

          # noqa: E501

        :return: The clickwrap_name of this ClickwrapResponse.  # noqa: E501
        :rtype: str
        """
        return self._clickwrap_name

    @clickwrap_name.setter
    def clickwrap_name(self, clickwrap_name):
        """Sets the clickwrap_name of this ClickwrapResponse.

          # noqa: E501

        :param clickwrap_name: The clickwrap_name of this ClickwrapResponse.  # noqa: E501
        :type: str
        """

        self._clickwrap_name = clickwrap_name

    @property
    def created_time(self):
        """Gets the created_time of this ClickwrapResponse.  # noqa: E501

          # noqa: E501

        :return: The created_time of this ClickwrapResponse.  # noqa: E501
        :rtype: object
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ClickwrapResponse.

          # noqa: E501

        :param created_time: The created_time of this ClickwrapResponse.  # noqa: E501
        :type: object
        """

        self._created_time = created_time

    @property
    def display_settings(self):
        """Gets the display_settings of this ClickwrapResponse.  # noqa: E501


        :return: The display_settings of this ClickwrapResponse.  # noqa: E501
        :rtype: DisplaySettings
        """
        return self._display_settings

    @display_settings.setter
    def display_settings(self, display_settings):
        """Sets the display_settings of this ClickwrapResponse.


        :param display_settings: The display_settings of this ClickwrapResponse.  # noqa: E501
        :type: DisplaySettings
        """

        self._display_settings = display_settings

    @property
    def documents(self):
        """Gets the documents of this ClickwrapResponse.  # noqa: E501

          # noqa: E501

        :return: The documents of this ClickwrapResponse.  # noqa: E501
        :rtype: list[Document]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this ClickwrapResponse.

          # noqa: E501

        :param documents: The documents of this ClickwrapResponse.  # noqa: E501
        :type: list[Document]
        """

        self._documents = documents

    @property
    def last_modified(self):
        """Gets the last_modified of this ClickwrapResponse.  # noqa: E501

          # noqa: E501

        :return: The last_modified of this ClickwrapResponse.  # noqa: E501
        :rtype: object
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this ClickwrapResponse.

          # noqa: E501

        :param last_modified: The last_modified of this ClickwrapResponse.  # noqa: E501
        :type: object
        """

        self._last_modified = last_modified

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this ClickwrapResponse.  # noqa: E501

          # noqa: E501

        :return: The last_modified_by of this ClickwrapResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this ClickwrapResponse.

          # noqa: E501

        :param last_modified_by: The last_modified_by of this ClickwrapResponse.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def owner_user_id(self):
        """Gets the owner_user_id of this ClickwrapResponse.  # noqa: E501

          # noqa: E501

        :return: The owner_user_id of this ClickwrapResponse.  # noqa: E501
        :rtype: str
        """
        return self._owner_user_id

    @owner_user_id.setter
    def owner_user_id(self, owner_user_id):
        """Sets the owner_user_id of this ClickwrapResponse.

          # noqa: E501

        :param owner_user_id: The owner_user_id of this ClickwrapResponse.  # noqa: E501
        :type: str
        """

        self._owner_user_id = owner_user_id

    @property
    def require_reacceptance(self):
        """Gets the require_reacceptance of this ClickwrapResponse.  # noqa: E501

          # noqa: E501

        :return: The require_reacceptance of this ClickwrapResponse.  # noqa: E501
        :rtype: bool
        """
        return self._require_reacceptance

    @require_reacceptance.setter
    def require_reacceptance(self, require_reacceptance):
        """Sets the require_reacceptance of this ClickwrapResponse.

          # noqa: E501

        :param require_reacceptance: The require_reacceptance of this ClickwrapResponse.  # noqa: E501
        :type: bool
        """

        self._require_reacceptance = require_reacceptance

    @property
    def scheduled_date(self):
        """Gets the scheduled_date of this ClickwrapResponse.  # noqa: E501

          # noqa: E501

        :return: The scheduled_date of this ClickwrapResponse.  # noqa: E501
        :rtype: object
        """
        return self._scheduled_date

    @scheduled_date.setter
    def scheduled_date(self, scheduled_date):
        """Sets the scheduled_date of this ClickwrapResponse.

          # noqa: E501

        :param scheduled_date: The scheduled_date of this ClickwrapResponse.  # noqa: E501
        :type: object
        """

        self._scheduled_date = scheduled_date

    @property
    def scheduled_reacceptance(self):
        """Gets the scheduled_reacceptance of this ClickwrapResponse.  # noqa: E501


        :return: The scheduled_reacceptance of this ClickwrapResponse.  # noqa: E501
        :rtype: ClickwrapScheduledReacceptance
        """
        return self._scheduled_reacceptance

    @scheduled_reacceptance.setter
    def scheduled_reacceptance(self, scheduled_reacceptance):
        """Sets the scheduled_reacceptance of this ClickwrapResponse.


        :param scheduled_reacceptance: The scheduled_reacceptance of this ClickwrapResponse.  # noqa: E501
        :type: ClickwrapScheduledReacceptance
        """

        self._scheduled_reacceptance = scheduled_reacceptance

    @property
    def status(self):
        """Gets the status of this ClickwrapResponse.  # noqa: E501

          # noqa: E501

        :return: The status of this ClickwrapResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClickwrapResponse.

          # noqa: E501

        :param status: The status of this ClickwrapResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def version_id(self):
        """Gets the version_id of this ClickwrapResponse.  # noqa: E501

          # noqa: E501

        :return: The version_id of this ClickwrapResponse.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this ClickwrapResponse.

          # noqa: E501

        :param version_id: The version_id of this ClickwrapResponse.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def version_number(self):
        """Gets the version_number of this ClickwrapResponse.  # noqa: E501

          # noqa: E501

        :return: The version_number of this ClickwrapResponse.  # noqa: E501
        :rtype: int
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this ClickwrapResponse.

          # noqa: E501

        :param version_number: The version_number of this ClickwrapResponse.  # noqa: E501
        :type: int
        """

        self._version_number = version_number

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ClickwrapResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClickwrapResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
