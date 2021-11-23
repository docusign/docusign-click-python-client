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


class ClickwrapAgreementsResponse(object):
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
        'begin_created_on': 'object',
        'minimum_pages_remaining': 'int',
        'page': 'int',
        'page_size': 'int',
        'user_agreements': 'list[UserAgreementResponse]'
    }

    attribute_map = {
        'begin_created_on': 'beginCreatedOn',
        'minimum_pages_remaining': 'minimumPagesRemaining',
        'page': 'page',
        'page_size': 'pageSize',
        'user_agreements': 'userAgreements'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ClickwrapAgreementsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._begin_created_on = None
        self._minimum_pages_remaining = None
        self._page = None
        self._page_size = None
        self._user_agreements = None
        self.discriminator = None

        setattr(self, "_{}".format('begin_created_on'), kwargs.get('begin_created_on', None))
        setattr(self, "_{}".format('minimum_pages_remaining'), kwargs.get('minimum_pages_remaining', None))
        setattr(self, "_{}".format('page'), kwargs.get('page', None))
        setattr(self, "_{}".format('page_size'), kwargs.get('page_size', None))
        setattr(self, "_{}".format('user_agreements'), kwargs.get('user_agreements', None))

    @property
    def begin_created_on(self):
        """Gets the begin_created_on of this ClickwrapAgreementsResponse.  # noqa: E501

          # noqa: E501

        :return: The begin_created_on of this ClickwrapAgreementsResponse.  # noqa: E501
        :rtype: object
        """
        return self._begin_created_on

    @begin_created_on.setter
    def begin_created_on(self, begin_created_on):
        """Sets the begin_created_on of this ClickwrapAgreementsResponse.

          # noqa: E501

        :param begin_created_on: The begin_created_on of this ClickwrapAgreementsResponse.  # noqa: E501
        :type: object
        """

        self._begin_created_on = begin_created_on

    @property
    def minimum_pages_remaining(self):
        """Gets the minimum_pages_remaining of this ClickwrapAgreementsResponse.  # noqa: E501

          # noqa: E501

        :return: The minimum_pages_remaining of this ClickwrapAgreementsResponse.  # noqa: E501
        :rtype: int
        """
        return self._minimum_pages_remaining

    @minimum_pages_remaining.setter
    def minimum_pages_remaining(self, minimum_pages_remaining):
        """Sets the minimum_pages_remaining of this ClickwrapAgreementsResponse.

          # noqa: E501

        :param minimum_pages_remaining: The minimum_pages_remaining of this ClickwrapAgreementsResponse.  # noqa: E501
        :type: int
        """

        self._minimum_pages_remaining = minimum_pages_remaining

    @property
    def page(self):
        """Gets the page of this ClickwrapAgreementsResponse.  # noqa: E501

          # noqa: E501

        :return: The page of this ClickwrapAgreementsResponse.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ClickwrapAgreementsResponse.

          # noqa: E501

        :param page: The page of this ClickwrapAgreementsResponse.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this ClickwrapAgreementsResponse.  # noqa: E501

          # noqa: E501

        :return: The page_size of this ClickwrapAgreementsResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ClickwrapAgreementsResponse.

          # noqa: E501

        :param page_size: The page_size of this ClickwrapAgreementsResponse.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def user_agreements(self):
        """Gets the user_agreements of this ClickwrapAgreementsResponse.  # noqa: E501

          # noqa: E501

        :return: The user_agreements of this ClickwrapAgreementsResponse.  # noqa: E501
        :rtype: list[UserAgreementResponse]
        """
        return self._user_agreements

    @user_agreements.setter
    def user_agreements(self, user_agreements):
        """Sets the user_agreements of this ClickwrapAgreementsResponse.

          # noqa: E501

        :param user_agreements: The user_agreements of this ClickwrapAgreementsResponse.  # noqa: E501
        :type: list[UserAgreementResponse]
        """

        self._user_agreements = user_agreements

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
        if issubclass(ClickwrapAgreementsResponse, dict):
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
        if not isinstance(other, ClickwrapAgreementsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClickwrapAgreementsResponse):
            return True

        return self.to_dict() != other.to_dict()
