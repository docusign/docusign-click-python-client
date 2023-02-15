# coding: utf-8

"""
    DocuSign Click API

    Elastic signing (also known as DocuSign Click)  lets you capture consent to standard agreement terms with a single click: terms and conditions, terms of service, terms of use, privacy policies, and more. The Click API lets you include this customizable elastic template solution in your DocuSign integrations.  # noqa: E501

    OpenAPI spec version: v1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_click.client.configuration import Configuration


class ClickwrapVersion(object):
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
        'clickwrap_version_id': 'str',
        'created_time': 'object',
        'data_fields': 'list[DataField]',
        'last_modified': 'object',
        'last_modified_by': 'str',
        'owner_user_id': 'str',
        'require_reacceptance': 'bool',
        'scheduled_date': 'object',
        'scheduled_reacceptance': 'ClickwrapScheduledReacceptance',
        'status': 'str',
        'version_id': 'str',
        'version_number': 'str'
    }

    attribute_map = {
        'clickwrap_version_id': 'clickwrapVersionId',
        'created_time': 'createdTime',
        'data_fields': 'dataFields',
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

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ClickwrapVersion - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._clickwrap_version_id = None
        self._created_time = None
        self._data_fields = None
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

        setattr(self, "_{}".format('clickwrap_version_id'), kwargs.get('clickwrap_version_id', None))
        setattr(self, "_{}".format('created_time'), kwargs.get('created_time', None))
        setattr(self, "_{}".format('data_fields'), kwargs.get('data_fields', None))
        setattr(self, "_{}".format('last_modified'), kwargs.get('last_modified', None))
        setattr(self, "_{}".format('last_modified_by'), kwargs.get('last_modified_by', None))
        setattr(self, "_{}".format('owner_user_id'), kwargs.get('owner_user_id', None))
        setattr(self, "_{}".format('require_reacceptance'), kwargs.get('require_reacceptance', None))
        setattr(self, "_{}".format('scheduled_date'), kwargs.get('scheduled_date', None))
        setattr(self, "_{}".format('scheduled_reacceptance'), kwargs.get('scheduled_reacceptance', None))
        setattr(self, "_{}".format('status'), kwargs.get('status', None))
        setattr(self, "_{}".format('version_id'), kwargs.get('version_id', None))
        setattr(self, "_{}".format('version_number'), kwargs.get('version_number', None))

    @property
    def clickwrap_version_id(self):
        """Gets the clickwrap_version_id of this ClickwrapVersion.  # noqa: E501

        The unique version ID, a GUID, of this clickwrap version.  # noqa: E501

        :return: The clickwrap_version_id of this ClickwrapVersion.  # noqa: E501
        :rtype: str
        """
        return self._clickwrap_version_id

    @clickwrap_version_id.setter
    def clickwrap_version_id(self, clickwrap_version_id):
        """Sets the clickwrap_version_id of this ClickwrapVersion.

        The unique version ID, a GUID, of this clickwrap version.  # noqa: E501

        :param clickwrap_version_id: The clickwrap_version_id of this ClickwrapVersion.  # noqa: E501
        :type: str
        """

        self._clickwrap_version_id = clickwrap_version_id

    @property
    def created_time(self):
        """Gets the created_time of this ClickwrapVersion.  # noqa: E501

        The time that the clickwrap was created.  # noqa: E501

        :return: The created_time of this ClickwrapVersion.  # noqa: E501
        :rtype: object
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ClickwrapVersion.

        The time that the clickwrap was created.  # noqa: E501

        :param created_time: The created_time of this ClickwrapVersion.  # noqa: E501
        :type: object
        """

        self._created_time = created_time

    @property
    def data_fields(self):
        """Gets the data_fields of this ClickwrapVersion.  # noqa: E501

        The list of all the data fields available for the clickwrap (custom fields and standard fields).  # noqa: E501

        :return: The data_fields of this ClickwrapVersion.  # noqa: E501
        :rtype: list[DataField]
        """
        return self._data_fields

    @data_fields.setter
    def data_fields(self, data_fields):
        """Sets the data_fields of this ClickwrapVersion.

        The list of all the data fields available for the clickwrap (custom fields and standard fields).  # noqa: E501

        :param data_fields: The data_fields of this ClickwrapVersion.  # noqa: E501
        :type: list[DataField]
        """

        self._data_fields = data_fields

    @property
    def last_modified(self):
        """Gets the last_modified of this ClickwrapVersion.  # noqa: E501

        The time that the clickwrap was last modified.  # noqa: E501

        :return: The last_modified of this ClickwrapVersion.  # noqa: E501
        :rtype: object
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this ClickwrapVersion.

        The time that the clickwrap was last modified.  # noqa: E501

        :param last_modified: The last_modified of this ClickwrapVersion.  # noqa: E501
        :type: object
        """

        self._last_modified = last_modified

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this ClickwrapVersion.  # noqa: E501

        The user ID of the last user who modified this clickwrap.  # noqa: E501

        :return: The last_modified_by of this ClickwrapVersion.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this ClickwrapVersion.

        The user ID of the last user who modified this clickwrap.  # noqa: E501

        :param last_modified_by: The last_modified_by of this ClickwrapVersion.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def owner_user_id(self):
        """Gets the owner_user_id of this ClickwrapVersion.  # noqa: E501

        The user ID of the owner of this clickwrap.  # noqa: E501

        :return: The owner_user_id of this ClickwrapVersion.  # noqa: E501
        :rtype: str
        """
        return self._owner_user_id

    @owner_user_id.setter
    def owner_user_id(self, owner_user_id):
        """Sets the owner_user_id of this ClickwrapVersion.

        The user ID of the owner of this clickwrap.  # noqa: E501

        :param owner_user_id: The owner_user_id of this ClickwrapVersion.  # noqa: E501
        :type: str
        """

        self._owner_user_id = owner_user_id

    @property
    def require_reacceptance(self):
        """Gets the require_reacceptance of this ClickwrapVersion.  # noqa: E501

        When **true,** requires signers who have previously agreed to this clickwrap to sign again. The version number is incremented.  # noqa: E501

        :return: The require_reacceptance of this ClickwrapVersion.  # noqa: E501
        :rtype: bool
        """
        return self._require_reacceptance

    @require_reacceptance.setter
    def require_reacceptance(self, require_reacceptance):
        """Sets the require_reacceptance of this ClickwrapVersion.

        When **true,** requires signers who have previously agreed to this clickwrap to sign again. The version number is incremented.  # noqa: E501

        :param require_reacceptance: The require_reacceptance of this ClickwrapVersion.  # noqa: E501
        :type: bool
        """

        self._require_reacceptance = require_reacceptance

    @property
    def scheduled_date(self):
        """Gets the scheduled_date of this ClickwrapVersion.  # noqa: E501

        The time and date when this clickwrap is activated.  # noqa: E501

        :return: The scheduled_date of this ClickwrapVersion.  # noqa: E501
        :rtype: object
        """
        return self._scheduled_date

    @scheduled_date.setter
    def scheduled_date(self, scheduled_date):
        """Sets the scheduled_date of this ClickwrapVersion.

        The time and date when this clickwrap is activated.  # noqa: E501

        :param scheduled_date: The scheduled_date of this ClickwrapVersion.  # noqa: E501
        :type: object
        """

        self._scheduled_date = scheduled_date

    @property
    def scheduled_reacceptance(self):
        """Gets the scheduled_reacceptance of this ClickwrapVersion.  # noqa: E501

        Specifies the interval between reacceptances in days, weeks, months, or years.  # noqa: E501

        :return: The scheduled_reacceptance of this ClickwrapVersion.  # noqa: E501
        :rtype: ClickwrapScheduledReacceptance
        """
        return self._scheduled_reacceptance

    @scheduled_reacceptance.setter
    def scheduled_reacceptance(self, scheduled_reacceptance):
        """Sets the scheduled_reacceptance of this ClickwrapVersion.

        Specifies the interval between reacceptances in days, weeks, months, or years.  # noqa: E501

        :param scheduled_reacceptance: The scheduled_reacceptance of this ClickwrapVersion.  # noqa: E501
        :type: ClickwrapScheduledReacceptance
        """

        self._scheduled_reacceptance = scheduled_reacceptance

    @property
    def status(self):
        """Gets the status of this ClickwrapVersion.  # noqa: E501

        Clickwrap status. Possible values:  - `active` - `inactive` - `deleted`  # noqa: E501

        :return: The status of this ClickwrapVersion.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClickwrapVersion.

        Clickwrap status. Possible values:  - `active` - `inactive` - `deleted`  # noqa: E501

        :param status: The status of this ClickwrapVersion.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def version_id(self):
        """Gets the version_id of this ClickwrapVersion.  # noqa: E501

        The ID of the version.  # noqa: E501

        :return: The version_id of this ClickwrapVersion.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this ClickwrapVersion.

        The ID of the version.  # noqa: E501

        :param version_id: The version_id of this ClickwrapVersion.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def version_number(self):
        """Gets the version_number of this ClickwrapVersion.  # noqa: E501

        Version of the clickwrap.  # noqa: E501

        :return: The version_number of this ClickwrapVersion.  # noqa: E501
        :rtype: str
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this ClickwrapVersion.

        Version of the clickwrap.  # noqa: E501

        :param version_number: The version_number of this ClickwrapVersion.  # noqa: E501
        :type: str
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
        if issubclass(ClickwrapVersion, dict):
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
        if not isinstance(other, ClickwrapVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClickwrapVersion):
            return True

        return self.to_dict() != other.to_dict()
