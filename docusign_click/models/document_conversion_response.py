# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DocumentConversionResponse(object):
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
        'html_results': 'list[HtmlResult]'
    }

    attribute_map = {
        'html_results': 'htmlResults'
    }

    def __init__(self, html_results=None):  # noqa: E501
        """DocumentConversionResponse - a model defined in Swagger"""  # noqa: E501

        self._html_results = None
        self.discriminator = None

        if html_results is not None:
            self.html_results = html_results

    @property
    def html_results(self):
        """Gets the html_results of this DocumentConversionResponse.  # noqa: E501

          # noqa: E501

        :return: The html_results of this DocumentConversionResponse.  # noqa: E501
        :rtype: list[HtmlResult]
        """
        return self._html_results

    @html_results.setter
    def html_results(self, html_results):
        """Sets the html_results of this DocumentConversionResponse.

          # noqa: E501

        :param html_results: The html_results of this DocumentConversionResponse.  # noqa: E501
        :type: list[HtmlResult]
        """

        self._html_results = html_results

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
        if issubclass(DocumentConversionResponse, dict):
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
        if not isinstance(other, DocumentConversionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
