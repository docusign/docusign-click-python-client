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


class ClickwrapScheduledReacceptance(object):
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
        'recurrence_interval': 'int',
        'recurrence_interval_type': 'str',
        'start_date_time': 'object'
    }

    attribute_map = {
        'recurrence_interval': 'recurrenceInterval',
        'recurrence_interval_type': 'recurrenceIntervalType',
        'start_date_time': 'startDateTime'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ClickwrapScheduledReacceptance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._recurrence_interval = None
        self._recurrence_interval_type = None
        self._start_date_time = None
        self.discriminator = None

        setattr(self, "_{}".format('recurrence_interval'), kwargs.get('recurrence_interval', None))
        setattr(self, "_{}".format('recurrence_interval_type'), kwargs.get('recurrence_interval_type', None))
        setattr(self, "_{}".format('start_date_time'), kwargs.get('start_date_time', None))

    @property
    def recurrence_interval(self):
        """Gets the recurrence_interval of this ClickwrapScheduledReacceptance.  # noqa: E501

        The time between recurrences specified in `recurrenceIntervalType` units.  The minimum and maximum values depend on `recurrenceIntervalType`:  - `days`: 1 - 365 - `weeks`: 1 - 52 - `months`: 1 - 12 - `years`: 1  # noqa: E501

        :return: The recurrence_interval of this ClickwrapScheduledReacceptance.  # noqa: E501
        :rtype: int
        """
        return self._recurrence_interval

    @recurrence_interval.setter
    def recurrence_interval(self, recurrence_interval):
        """Sets the recurrence_interval of this ClickwrapScheduledReacceptance.

        The time between recurrences specified in `recurrenceIntervalType` units.  The minimum and maximum values depend on `recurrenceIntervalType`:  - `days`: 1 - 365 - `weeks`: 1 - 52 - `months`: 1 - 12 - `years`: 1  # noqa: E501

        :param recurrence_interval: The recurrence_interval of this ClickwrapScheduledReacceptance.  # noqa: E501
        :type: int
        """

        self._recurrence_interval = recurrence_interval

    @property
    def recurrence_interval_type(self):
        """Gets the recurrence_interval_type of this ClickwrapScheduledReacceptance.  # noqa: E501

        The units of the `recurrenceInterval`. Must be one of:  - `days` - `weeks` - `month` - `years`   # noqa: E501

        :return: The recurrence_interval_type of this ClickwrapScheduledReacceptance.  # noqa: E501
        :rtype: str
        """
        return self._recurrence_interval_type

    @recurrence_interval_type.setter
    def recurrence_interval_type(self, recurrence_interval_type):
        """Sets the recurrence_interval_type of this ClickwrapScheduledReacceptance.

        The units of the `recurrenceInterval`. Must be one of:  - `days` - `weeks` - `month` - `years`   # noqa: E501

        :param recurrence_interval_type: The recurrence_interval_type of this ClickwrapScheduledReacceptance.  # noqa: E501
        :type: str
        """

        self._recurrence_interval_type = recurrence_interval_type

    @property
    def start_date_time(self):
        """Gets the start_date_time of this ClickwrapScheduledReacceptance.  # noqa: E501

        The date when the recurrence interval starts.  # noqa: E501

        :return: The start_date_time of this ClickwrapScheduledReacceptance.  # noqa: E501
        :rtype: object
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this ClickwrapScheduledReacceptance.

        The date when the recurrence interval starts.  # noqa: E501

        :param start_date_time: The start_date_time of this ClickwrapScheduledReacceptance.  # noqa: E501
        :type: object
        """

        self._start_date_time = start_date_time

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
        if issubclass(ClickwrapScheduledReacceptance, dict):
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
        if not isinstance(other, ClickwrapScheduledReacceptance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClickwrapScheduledReacceptance):
            return True

        return self.to_dict() != other.to_dict()
