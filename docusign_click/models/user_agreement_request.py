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
        'host_origin': 'str',
        'metadata': 'str'
    }

    attribute_map = {
        'client_user_id': 'clientUserId',
        'host_origin': 'hostOrigin',
        'metadata': 'metadata'
    }

    def __init__(self, client_user_id=None, host_origin=None, metadata=None):  # noqa: E501
        """UserAgreementRequest - a model defined in Swagger"""  # noqa: E501

        self._client_user_id = None
        self._host_origin = None
        self._metadata = None
        self.discriminator = None

        if client_user_id is not None:
            self.client_user_id = client_user_id
        if host_origin is not None:
            self.host_origin = host_origin
        if metadata is not None:
            self.metadata = metadata

    @property
    def client_user_id(self):
        """Gets the client_user_id of this UserAgreementRequest.  # noqa: E501

          # noqa: E501

        :return: The client_user_id of this UserAgreementRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_user_id

    @client_user_id.setter
    def client_user_id(self, client_user_id):
        """Sets the client_user_id of this UserAgreementRequest.

          # noqa: E501

        :param client_user_id: The client_user_id of this UserAgreementRequest.  # noqa: E501
        :type: str
        """

        self._client_user_id = client_user_id

    @property
    def host_origin(self):
        """Gets the host_origin of this UserAgreementRequest.  # noqa: E501

          # noqa: E501

        :return: The host_origin of this UserAgreementRequest.  # noqa: E501
        :rtype: str
        """
        return self._host_origin

    @host_origin.setter
    def host_origin(self, host_origin):
        """Sets the host_origin of this UserAgreementRequest.

          # noqa: E501

        :param host_origin: The host_origin of this UserAgreementRequest.  # noqa: E501
        :type: str
        """

        self._host_origin = host_origin

    @property
    def metadata(self):
        """Gets the metadata of this UserAgreementRequest.  # noqa: E501

          # noqa: E501

        :return: The metadata of this UserAgreementRequest.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this UserAgreementRequest.

          # noqa: E501

        :param metadata: The metadata of this UserAgreementRequest.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

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

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
