# coding: utf-8

"""
    DocuSign Click API

    DocuSign Click lets you capture consent to standard agreement terms with a single click: terms and conditions, terms of service, terms of use, privacy policies, and more. The Click API lets you include this customizable clickwrap solution in your DocuSign integrations.  # noqa: E501

    OpenAPI spec version: v1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_click.client.configuration import Configuration


class ClickwrapDeleteResponse(object):
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
        'clickwrap_id': 'str',
        'clickwrap_name': 'str',
        'deletion_message': 'str',
        'deletion_success': 'bool',
        'status': 'str'
    }

    attribute_map = {
        'clickwrap_id': 'clickwrapId',
        'clickwrap_name': 'clickwrapName',
        'deletion_message': 'deletionMessage',
        'deletion_success': 'deletionSuccess',
        'status': 'status'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ClickwrapDeleteResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._clickwrap_id = None
        self._clickwrap_name = None
        self._deletion_message = None
        self._deletion_success = None
        self._status = None
        self.discriminator = None

        setattr(self, "_{}".format('clickwrap_id'), kwargs.get('clickwrap_id', None))
        setattr(self, "_{}".format('clickwrap_name'), kwargs.get('clickwrap_name', None))
        setattr(self, "_{}".format('deletion_message'), kwargs.get('deletion_message', None))
        setattr(self, "_{}".format('deletion_success'), kwargs.get('deletion_success', None))
        setattr(self, "_{}".format('status'), kwargs.get('status', None))

    @property
    def clickwrap_id(self):
        """Gets the clickwrap_id of this ClickwrapDeleteResponse.  # noqa: E501

        The ID of the clickwrap.  # noqa: E501

        :return: The clickwrap_id of this ClickwrapDeleteResponse.  # noqa: E501
        :rtype: str
        """
        return self._clickwrap_id

    @clickwrap_id.setter
    def clickwrap_id(self, clickwrap_id):
        """Sets the clickwrap_id of this ClickwrapDeleteResponse.

        The ID of the clickwrap.  # noqa: E501

        :param clickwrap_id: The clickwrap_id of this ClickwrapDeleteResponse.  # noqa: E501
        :type: str
        """

        self._clickwrap_id = clickwrap_id

    @property
    def clickwrap_name(self):
        """Gets the clickwrap_name of this ClickwrapDeleteResponse.  # noqa: E501

        The name of the clickwrap.  # noqa: E501

        :return: The clickwrap_name of this ClickwrapDeleteResponse.  # noqa: E501
        :rtype: str
        """
        return self._clickwrap_name

    @clickwrap_name.setter
    def clickwrap_name(self, clickwrap_name):
        """Sets the clickwrap_name of this ClickwrapDeleteResponse.

        The name of the clickwrap.  # noqa: E501

        :param clickwrap_name: The clickwrap_name of this ClickwrapDeleteResponse.  # noqa: E501
        :type: str
        """

        self._clickwrap_name = clickwrap_name

    @property
    def deletion_message(self):
        """Gets the deletion_message of this ClickwrapDeleteResponse.  # noqa: E501

        A message describing the result of deletion request. One of:  - `alreadyDeleted`: Clickwrap is already deleted. - `deletionSuccess`: Successfully deleted the clickwrap. - `deletionFailure`: Failed to delete the clickwrap. - `cannotDelete`: Active clickwrap version cannot be deleted.  # noqa: E501

        :return: The deletion_message of this ClickwrapDeleteResponse.  # noqa: E501
        :rtype: str
        """
        return self._deletion_message

    @deletion_message.setter
    def deletion_message(self, deletion_message):
        """Sets the deletion_message of this ClickwrapDeleteResponse.

        A message describing the result of deletion request. One of:  - `alreadyDeleted`: Clickwrap is already deleted. - `deletionSuccess`: Successfully deleted the clickwrap. - `deletionFailure`: Failed to delete the clickwrap. - `cannotDelete`: Active clickwrap version cannot be deleted.  # noqa: E501

        :param deletion_message: The deletion_message of this ClickwrapDeleteResponse.  # noqa: E501
        :type: str
        """

        self._deletion_message = deletion_message

    @property
    def deletion_success(self):
        """Gets the deletion_success of this ClickwrapDeleteResponse.  # noqa: E501

        **True** if the clickwrap was deleted successfully. **False** otherwise.  # noqa: E501

        :return: The deletion_success of this ClickwrapDeleteResponse.  # noqa: E501
        :rtype: bool
        """
        return self._deletion_success

    @deletion_success.setter
    def deletion_success(self, deletion_success):
        """Sets the deletion_success of this ClickwrapDeleteResponse.

        **True** if the clickwrap was deleted successfully. **False** otherwise.  # noqa: E501

        :param deletion_success: The deletion_success of this ClickwrapDeleteResponse.  # noqa: E501
        :type: bool
        """

        self._deletion_success = deletion_success

    @property
    def status(self):
        """Gets the status of this ClickwrapDeleteResponse.  # noqa: E501

        Clickwrap status. Possible values:  - `active` - `inactive` - `deleted`  # noqa: E501

        :return: The status of this ClickwrapDeleteResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClickwrapDeleteResponse.

        Clickwrap status. Possible values:  - `active` - `inactive` - `deleted`  # noqa: E501

        :param status: The status of this ClickwrapDeleteResponse.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(ClickwrapDeleteResponse, dict):
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
        if not isinstance(other, ClickwrapDeleteResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClickwrapDeleteResponse):
            return True

        return self.to_dict() != other.to_dict()
