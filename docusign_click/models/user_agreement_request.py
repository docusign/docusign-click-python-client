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


class UserAgreementRequest(object):
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
        'client_user_id': 'str',
        'document_data': 'dict(str, object)',
        'metadata': 'str',
        'return_url': 'str'
    }

    attribute_map = {
        'client_user_id': 'clientUserId',
        'document_data': 'documentData',
        'metadata': 'metadata',
        'return_url': 'returnUrl'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """UserAgreementRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_user_id = None
        self._document_data = None
        self._metadata = None
        self._return_url = None
        self.discriminator = None

        setattr(self, "_{}".format('client_user_id'), kwargs.get('client_user_id', None))
        setattr(self, "_{}".format('document_data'), kwargs.get('document_data', None))
        setattr(self, "_{}".format('metadata'), kwargs.get('metadata', None))
        setattr(self, "_{}".format('return_url'), kwargs.get('return_url', None))

    @property
    def client_user_id(self):
        """Gets the client_user_id of this UserAgreementRequest.  # noqa: E501

        A unique value that identifies a user. You can use anything that your system uses to identify unique users, such as employee IDs, email addresses, and surrogate keys as the value of `clientUserId`.  A clickwrap with a specific `clientUserId` will not appear again once it has been accepted.   # noqa: E501

        :return: The client_user_id of this UserAgreementRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_user_id

    @client_user_id.setter
    def client_user_id(self, client_user_id):
        """Sets the client_user_id of this UserAgreementRequest.

        A unique value that identifies a user. You can use anything that your system uses to identify unique users, such as employee IDs, email addresses, and surrogate keys as the value of `clientUserId`.  A clickwrap with a specific `clientUserId` will not appear again once it has been accepted.   # noqa: E501

        :param client_user_id: The client_user_id of this UserAgreementRequest.  # noqa: E501
        :type: str
        """

        self._client_user_id = client_user_id

    @property
    def document_data(self):
        """Gets the document_data of this UserAgreementRequest.  # noqa: E501

        This property specifies the data used to create a clickwrap with [dynamic content][].    [dynamic content]: /docs/click-api/click101/customize-clickwrap-fields/#embed-clickwraps-that-contain-dynamic-content   # noqa: E501

        :return: The document_data of this UserAgreementRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._document_data

    @document_data.setter
    def document_data(self, document_data):
        """Sets the document_data of this UserAgreementRequest.

        This property specifies the data used to create a clickwrap with [dynamic content][].    [dynamic content]: /docs/click-api/click101/customize-clickwrap-fields/#embed-clickwraps-that-contain-dynamic-content   # noqa: E501

        :param document_data: The document_data of this UserAgreementRequest.  # noqa: E501
        :type: dict(str, object)
        """

        self._document_data = document_data

    @property
    def metadata(self):
        """Gets the metadata of this UserAgreementRequest.  # noqa: E501

        A customer-defined string you can use in requests. This string will appear in the corresponding response.  # noqa: E501

        :return: The metadata of this UserAgreementRequest.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this UserAgreementRequest.

        A customer-defined string you can use in requests. This string will appear in the corresponding response.  # noqa: E501

        :param metadata: The metadata of this UserAgreementRequest.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def return_url(self):
        """Gets the return_url of this UserAgreementRequest.  # noqa: E501

        The URL to redirect to after the agreement is complete when the agreement is not rendered in an iframe.  # noqa: E501

        :return: The return_url of this UserAgreementRequest.  # noqa: E501
        :rtype: str
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """Sets the return_url of this UserAgreementRequest.

        The URL to redirect to after the agreement is complete when the agreement is not rendered in an iframe.  # noqa: E501

        :param return_url: The return_url of this UserAgreementRequest.  # noqa: E501
        :type: str
        """

        self._return_url = return_url

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
        if issubclass(UserAgreementRequest, dict):
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
        if not isinstance(other, UserAgreementRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserAgreementRequest):
            return True

        return self.to_dict() != other.to_dict()
