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


class BulkClickwrapRequest(object):
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
        'from_date': 'object',
        'status': 'str',
        'to_date': 'object'
    }

    attribute_map = {
        'from_date': 'fromDate',
        'status': 'status',
        'to_date': 'toDate'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BulkClickwrapRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._from_date = None
        self._status = None
        self._to_date = None
        self.discriminator = None

        setattr(self, "_{}".format('from_date'), kwargs.get('from_date', None))
        setattr(self, "_{}".format('status'), kwargs.get('status', None))
        setattr(self, "_{}".format('to_date'), kwargs.get('to_date', None))

    @property
    def from_date(self):
        """Gets the from_date of this BulkClickwrapRequest.  # noqa: E501

        The earliest date to return agreements from.  # noqa: E501

        :return: The from_date of this BulkClickwrapRequest.  # noqa: E501
        :rtype: object
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this BulkClickwrapRequest.

        The earliest date to return agreements from.  # noqa: E501

        :param from_date: The from_date of this BulkClickwrapRequest.  # noqa: E501
        :type: object
        """

        self._from_date = from_date

    @property
    def status(self):
        """Gets the status of this BulkClickwrapRequest.  # noqa: E501

        User agreement status. One of:  - `agreed` - `declined`  # noqa: E501

        :return: The status of this BulkClickwrapRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BulkClickwrapRequest.

        User agreement status. One of:  - `agreed` - `declined`  # noqa: E501

        :param status: The status of this BulkClickwrapRequest.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def to_date(self):
        """Gets the to_date of this BulkClickwrapRequest.  # noqa: E501

        The latest date to return agreements from.  # noqa: E501

        :return: The to_date of this BulkClickwrapRequest.  # noqa: E501
        :rtype: object
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this BulkClickwrapRequest.

        The latest date to return agreements from.  # noqa: E501

        :param to_date: The to_date of this BulkClickwrapRequest.  # noqa: E501
        :type: object
        """

        self._to_date = to_date

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
        if issubclass(BulkClickwrapRequest, dict):
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
        if not isinstance(other, BulkClickwrapRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkClickwrapRequest):
            return True

        return self.to_dict() != other.to_dict()
