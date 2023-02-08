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


class Document(object):
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
        'document_base64': 'str',
        'document_display': 'str',
        'document_html': 'str',
        'document_name': 'str',
        'file_extension': 'str',
        'must_read': 'bool',
        'must_view': 'bool',
        'order': 'int'
    }

    attribute_map = {
        'document_base64': 'documentBase64',
        'document_display': 'documentDisplay',
        'document_html': 'documentHtml',
        'document_name': 'documentName',
        'file_extension': 'fileExtension',
        'must_read': 'mustRead',
        'must_view': 'mustView',
        'order': 'order'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """Document - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._document_base64 = None
        self._document_display = None
        self._document_html = None
        self._document_name = None
        self._file_extension = None
        self._must_read = None
        self._must_view = None
        self._order = None
        self.discriminator = None

        setattr(self, "_{}".format('document_base64'), kwargs.get('document_base64', None))
        setattr(self, "_{}".format('document_display'), kwargs.get('document_display', None))
        setattr(self, "_{}".format('document_html'), kwargs.get('document_html', None))
        setattr(self, "_{}".format('document_name'), kwargs.get('document_name', None))
        setattr(self, "_{}".format('file_extension'), kwargs.get('file_extension', None))
        setattr(self, "_{}".format('must_read'), kwargs.get('must_read', None))
        setattr(self, "_{}".format('must_view'), kwargs.get('must_view', None))
        setattr(self, "_{}".format('order'), kwargs.get('order', None))

    @property
    def document_base64(self):
        """Gets the document_base64 of this Document.  # noqa: E501

        The base64-encoded contents of the document.  # noqa: E501

        :return: The document_base64 of this Document.  # noqa: E501
        :rtype: str
        """
        return self._document_base64

    @document_base64.setter
    def document_base64(self, document_base64):
        """Sets the document_base64 of this Document.

        The base64-encoded contents of the document.  # noqa: E501

        :param document_base64: The document_base64 of this Document.  # noqa: E501
        :type: str
        """

        self._document_base64 = document_base64

    @property
    def document_display(self):
        """Gets the document_display of this Document.  # noqa: E501

        Display type: link, document or pdf  # noqa: E501

        :return: The document_display of this Document.  # noqa: E501
        :rtype: str
        """
        return self._document_display

    @document_display.setter
    def document_display(self, document_display):
        """Sets the document_display of this Document.

        Display type: link, document or pdf  # noqa: E501

        :param document_display: The document_display of this Document.  # noqa: E501
        :type: str
        """

        self._document_display = document_display

    @property
    def document_html(self):
        """Gets the document_html of this Document.  # noqa: E501

        The HTML representation of the document.  # noqa: E501

        :return: The document_html of this Document.  # noqa: E501
        :rtype: str
        """
        return self._document_html

    @document_html.setter
    def document_html(self, document_html):
        """Sets the document_html of this Document.

        The HTML representation of the document.  # noqa: E501

        :param document_html: The document_html of this Document.  # noqa: E501
        :type: str
        """

        self._document_html = document_html

    @property
    def document_name(self):
        """Gets the document_name of this Document.  # noqa: E501

        The name of the document.  # noqa: E501

        :return: The document_name of this Document.  # noqa: E501
        :rtype: str
        """
        return self._document_name

    @document_name.setter
    def document_name(self, document_name):
        """Sets the document_name of this Document.

        The name of the document.  # noqa: E501

        :param document_name: The document_name of this Document.  # noqa: E501
        :type: str
        """

        self._document_name = document_name

    @property
    def file_extension(self):
        """Gets the file_extension of this Document.  # noqa: E501

        The file extension of the document.  # noqa: E501

        :return: The file_extension of this Document.  # noqa: E501
        :rtype: str
        """
        return self._file_extension

    @file_extension.setter
    def file_extension(self, file_extension):
        """Sets the file_extension of this Document.

        The file extension of the document.  # noqa: E501

        :param file_extension: The file_extension of this Document.  # noqa: E501
        :type: str
        """

        self._file_extension = file_extension

    @property
    def must_read(self):
        """Gets the must_read of this Document.  # noqa: E501

        **True** if the user needs to scroll to the end of the document.  # noqa: E501

        :return: The must_read of this Document.  # noqa: E501
        :rtype: bool
        """
        return self._must_read

    @must_read.setter
    def must_read(self, must_read):
        """Sets the must_read of this Document.

        **True** if the user needs to scroll to the end of the document.  # noqa: E501

        :param must_read: The must_read of this Document.  # noqa: E501
        :type: bool
        """

        self._must_read = must_read

    @property
    def must_view(self):
        """Gets the must_view of this Document.  # noqa: E501

        **True** if the user must view the document.  # noqa: E501

        :return: The must_view of this Document.  # noqa: E501
        :rtype: bool
        """
        return self._must_view

    @must_view.setter
    def must_view(self, must_view):
        """Sets the must_view of this Document.

        **True** if the user must view the document.  # noqa: E501

        :param must_view: The must_view of this Document.  # noqa: E501
        :type: bool
        """

        self._must_view = must_view

    @property
    def order(self):
        """Gets the order of this Document.  # noqa: E501

        The order of document layout.  # noqa: E501

        :return: The order of this Document.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this Document.

        The order of document layout.  # noqa: E501

        :param order: The order of this Document.  # noqa: E501
        :type: int
        """

        self._order = order

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
        if issubclass(Document, dict):
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
        if not isinstance(other, Document):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Document):
            return True

        return self.to_dict() != other.to_dict()
