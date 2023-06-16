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


class DocumentLinkStyles(object):
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
        'focus': 'DocumentLinkStylesFocus',
        'hover': 'DocumentLinkStylesFocus',
        'border': 'str',
        'color': 'str',
        'font_family': 'str',
        'font_size': 'str',
        'font_style': 'str',
        'font_weight': 'object',
        'margin': 'str',
        'padding': 'str',
        'text_decoration': 'str'
    }

    attribute_map = {
        'focus': ':focus',
        'hover': ':hover',
        'border': 'border',
        'color': 'color',
        'font_family': 'fontFamily',
        'font_size': 'fontSize',
        'font_style': 'fontStyle',
        'font_weight': 'fontWeight',
        'margin': 'margin',
        'padding': 'padding',
        'text_decoration': 'textDecoration'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DocumentLinkStyles - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._focus = None
        self._hover = None
        self._border = None
        self._color = None
        self._font_family = None
        self._font_size = None
        self._font_style = None
        self._font_weight = None
        self._margin = None
        self._padding = None
        self._text_decoration = None
        self.discriminator = None

        setattr(self, "_{}".format('focus'), kwargs.get('focus', None))
        setattr(self, "_{}".format('hover'), kwargs.get('hover', None))
        setattr(self, "_{}".format('border'), kwargs.get('border', None))
        setattr(self, "_{}".format('color'), kwargs.get('color', None))
        setattr(self, "_{}".format('font_family'), kwargs.get('font_family', None))
        setattr(self, "_{}".format('font_size'), kwargs.get('font_size', None))
        setattr(self, "_{}".format('font_style'), kwargs.get('font_style', None))
        setattr(self, "_{}".format('font_weight'), kwargs.get('font_weight', None))
        setattr(self, "_{}".format('margin'), kwargs.get('margin', None))
        setattr(self, "_{}".format('padding'), kwargs.get('padding', None))
        setattr(self, "_{}".format('text_decoration'), kwargs.get('text_decoration', None))

    @property
    def focus(self):
        """Gets the focus of this DocumentLinkStyles.  # noqa: E501


        :return: The focus of this DocumentLinkStyles.  # noqa: E501
        :rtype: DocumentLinkStylesFocus
        """
        return self._focus

    @focus.setter
    def focus(self, focus):
        """Sets the focus of this DocumentLinkStyles.


        :param focus: The focus of this DocumentLinkStyles.  # noqa: E501
        :type: DocumentLinkStylesFocus
        """

        self._focus = focus

    @property
    def hover(self):
        """Gets the hover of this DocumentLinkStyles.  # noqa: E501


        :return: The hover of this DocumentLinkStyles.  # noqa: E501
        :rtype: DocumentLinkStylesFocus
        """
        return self._hover

    @hover.setter
    def hover(self, hover):
        """Sets the hover of this DocumentLinkStyles.


        :param hover: The hover of this DocumentLinkStyles.  # noqa: E501
        :type: DocumentLinkStylesFocus
        """

        self._hover = hover

    @property
    def border(self):
        """Gets the border of this DocumentLinkStyles.  # noqa: E501

        Control the border of the element.  # noqa: E501

        :return: The border of this DocumentLinkStyles.  # noqa: E501
        :rtype: str
        """
        return self._border

    @border.setter
    def border(self, border):
        """Sets the border of this DocumentLinkStyles.

        Control the border of the element.  # noqa: E501

        :param border: The border of this DocumentLinkStyles.  # noqa: E501
        :type: str
        """

        self._border = border

    @property
    def color(self):
        """Gets the color of this DocumentLinkStyles.  # noqa: E501

        Control the fore-ground color of the element.  # noqa: E501

        :return: The color of this DocumentLinkStyles.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this DocumentLinkStyles.

        Control the fore-ground color of the element.  # noqa: E501

        :param color: The color of this DocumentLinkStyles.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def font_family(self):
        """Gets the font_family of this DocumentLinkStyles.  # noqa: E501

        Control the font family of the text.  # noqa: E501

        :return: The font_family of this DocumentLinkStyles.  # noqa: E501
        :rtype: str
        """
        return self._font_family

    @font_family.setter
    def font_family(self, font_family):
        """Sets the font_family of this DocumentLinkStyles.

        Control the font family of the text.  # noqa: E501

        :param font_family: The font_family of this DocumentLinkStyles.  # noqa: E501
        :type: str
        """

        self._font_family = font_family

    @property
    def font_size(self):
        """Gets the font_size of this DocumentLinkStyles.  # noqa: E501

        Control the font size of the text.  # noqa: E501

        :return: The font_size of this DocumentLinkStyles.  # noqa: E501
        :rtype: str
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this DocumentLinkStyles.

        Control the font size of the text.  # noqa: E501

        :param font_size: The font_size of this DocumentLinkStyles.  # noqa: E501
        :type: str
        """

        self._font_size = font_size

    @property
    def font_style(self):
        """Gets the font_style of this DocumentLinkStyles.  # noqa: E501

        Control the font style of the text.  # noqa: E501

        :return: The font_style of this DocumentLinkStyles.  # noqa: E501
        :rtype: str
        """
        return self._font_style

    @font_style.setter
    def font_style(self, font_style):
        """Sets the font_style of this DocumentLinkStyles.

        Control the font style of the text.  # noqa: E501

        :param font_style: The font_style of this DocumentLinkStyles.  # noqa: E501
        :type: str
        """

        self._font_style = font_style

    @property
    def font_weight(self):
        """Gets the font_weight of this DocumentLinkStyles.  # noqa: E501

        Control the font weight of the text.  # noqa: E501

        :return: The font_weight of this DocumentLinkStyles.  # noqa: E501
        :rtype: object
        """
        return self._font_weight

    @font_weight.setter
    def font_weight(self, font_weight):
        """Sets the font_weight of this DocumentLinkStyles.

        Control the font weight of the text.  # noqa: E501

        :param font_weight: The font_weight of this DocumentLinkStyles.  # noqa: E501
        :type: object
        """

        self._font_weight = font_weight

    @property
    def margin(self):
        """Gets the margin of this DocumentLinkStyles.  # noqa: E501

        Control the margin of the element.  # noqa: E501

        :return: The margin of this DocumentLinkStyles.  # noqa: E501
        :rtype: str
        """
        return self._margin

    @margin.setter
    def margin(self, margin):
        """Sets the margin of this DocumentLinkStyles.

        Control the margin of the element.  # noqa: E501

        :param margin: The margin of this DocumentLinkStyles.  # noqa: E501
        :type: str
        """

        self._margin = margin

    @property
    def padding(self):
        """Gets the padding of this DocumentLinkStyles.  # noqa: E501

        Control the padding of the element.  # noqa: E501

        :return: The padding of this DocumentLinkStyles.  # noqa: E501
        :rtype: str
        """
        return self._padding

    @padding.setter
    def padding(self, padding):
        """Sets the padding of this DocumentLinkStyles.

        Control the padding of the element.  # noqa: E501

        :param padding: The padding of this DocumentLinkStyles.  # noqa: E501
        :type: str
        """

        self._padding = padding

    @property
    def text_decoration(self):
        """Gets the text_decoration of this DocumentLinkStyles.  # noqa: E501

        Control the underline and other styles of the text.  # noqa: E501

        :return: The text_decoration of this DocumentLinkStyles.  # noqa: E501
        :rtype: str
        """
        return self._text_decoration

    @text_decoration.setter
    def text_decoration(self, text_decoration):
        """Sets the text_decoration of this DocumentLinkStyles.

        Control the underline and other styles of the text.  # noqa: E501

        :param text_decoration: The text_decoration of this DocumentLinkStyles.  # noqa: E501
        :type: str
        """

        self._text_decoration = text_decoration

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
        if issubclass(DocumentLinkStyles, dict):
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
        if not isinstance(other, DocumentLinkStyles):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentLinkStyles):
            return True

        return self.to_dict() != other.to_dict()
