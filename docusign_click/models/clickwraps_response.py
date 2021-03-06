# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ClickwrapsResponse(object):
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
        'clickwraps': 'list[ClickwrapSummaryResponse]',
        'minimum_pages_remaining': 'int',
        'page': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'clickwraps': 'clickwraps',
        'minimum_pages_remaining': 'minimumPagesRemaining',
        'page': 'page',
        'page_size': 'pageSize'
    }

    def __init__(self, clickwraps=None, minimum_pages_remaining=None, page=None, page_size=None):  # noqa: E501
        """ClickwrapsResponse - a model defined in Swagger"""  # noqa: E501

        self._clickwraps = None
        self._minimum_pages_remaining = None
        self._page = None
        self._page_size = None
        self.discriminator = None

        if clickwraps is not None:
            self.clickwraps = clickwraps
        if minimum_pages_remaining is not None:
            self.minimum_pages_remaining = minimum_pages_remaining
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size

    @property
    def clickwraps(self):
        """Gets the clickwraps of this ClickwrapsResponse.  # noqa: E501

          # noqa: E501

        :return: The clickwraps of this ClickwrapsResponse.  # noqa: E501
        :rtype: list[ClickwrapSummaryResponse]
        """
        return self._clickwraps

    @clickwraps.setter
    def clickwraps(self, clickwraps):
        """Sets the clickwraps of this ClickwrapsResponse.

          # noqa: E501

        :param clickwraps: The clickwraps of this ClickwrapsResponse.  # noqa: E501
        :type: list[ClickwrapSummaryResponse]
        """

        self._clickwraps = clickwraps

    @property
    def minimum_pages_remaining(self):
        """Gets the minimum_pages_remaining of this ClickwrapsResponse.  # noqa: E501

          # noqa: E501

        :return: The minimum_pages_remaining of this ClickwrapsResponse.  # noqa: E501
        :rtype: int
        """
        return self._minimum_pages_remaining

    @minimum_pages_remaining.setter
    def minimum_pages_remaining(self, minimum_pages_remaining):
        """Sets the minimum_pages_remaining of this ClickwrapsResponse.

          # noqa: E501

        :param minimum_pages_remaining: The minimum_pages_remaining of this ClickwrapsResponse.  # noqa: E501
        :type: int
        """

        self._minimum_pages_remaining = minimum_pages_remaining

    @property
    def page(self):
        """Gets the page of this ClickwrapsResponse.  # noqa: E501

          # noqa: E501

        :return: The page of this ClickwrapsResponse.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ClickwrapsResponse.

          # noqa: E501

        :param page: The page of this ClickwrapsResponse.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this ClickwrapsResponse.  # noqa: E501

          # noqa: E501

        :return: The page_size of this ClickwrapsResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ClickwrapsResponse.

          # noqa: E501

        :param page_size: The page_size of this ClickwrapsResponse.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

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
        if issubclass(ClickwrapsResponse, dict):
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
        if not isinstance(other, ClickwrapsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
