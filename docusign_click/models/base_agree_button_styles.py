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


class BaseAgreeButtonStyles(object):
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
        'background_color': 'str',
        'border': 'str',
        'border_color': 'str',
        'border_radius': 'str',
        'border_style': 'str',
        'border_width': 'str',
        'box_shadow': 'str',
        'color': 'str',
        'font_family': 'str',
        'font_size': 'str',
        'font_style': 'str',
        'font_weight': 'object',
        'height': 'str',
        'margin': 'str',
        'opacity': 'str',
        'outline': 'str',
        'outline_offset': 'str',
        'padding': 'str',
        'width': 'str'
    }

    attribute_map = {
        'background_color': 'backgroundColor',
        'border': 'border',
        'border_color': 'borderColor',
        'border_radius': 'borderRadius',
        'border_style': 'borderStyle',
        'border_width': 'borderWidth',
        'box_shadow': 'boxShadow',
        'color': 'color',
        'font_family': 'fontFamily',
        'font_size': 'fontSize',
        'font_style': 'fontStyle',
        'font_weight': 'fontWeight',
        'height': 'height',
        'margin': 'margin',
        'opacity': 'opacity',
        'outline': 'outline',
        'outline_offset': 'outlineOffset',
        'padding': 'padding',
        'width': 'width'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BaseAgreeButtonStyles - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._background_color = None
        self._border = None
        self._border_color = None
        self._border_radius = None
        self._border_style = None
        self._border_width = None
        self._box_shadow = None
        self._color = None
        self._font_family = None
        self._font_size = None
        self._font_style = None
        self._font_weight = None
        self._height = None
        self._margin = None
        self._opacity = None
        self._outline = None
        self._outline_offset = None
        self._padding = None
        self._width = None
        self.discriminator = None

        setattr(self, "_{}".format('background_color'), kwargs.get('background_color', None))
        setattr(self, "_{}".format('border'), kwargs.get('border', None))
        setattr(self, "_{}".format('border_color'), kwargs.get('border_color', None))
        setattr(self, "_{}".format('border_radius'), kwargs.get('border_radius', None))
        setattr(self, "_{}".format('border_style'), kwargs.get('border_style', None))
        setattr(self, "_{}".format('border_width'), kwargs.get('border_width', None))
        setattr(self, "_{}".format('box_shadow'), kwargs.get('box_shadow', None))
        setattr(self, "_{}".format('color'), kwargs.get('color', None))
        setattr(self, "_{}".format('font_family'), kwargs.get('font_family', None))
        setattr(self, "_{}".format('font_size'), kwargs.get('font_size', None))
        setattr(self, "_{}".format('font_style'), kwargs.get('font_style', None))
        setattr(self, "_{}".format('font_weight'), kwargs.get('font_weight', None))
        setattr(self, "_{}".format('height'), kwargs.get('height', None))
        setattr(self, "_{}".format('margin'), kwargs.get('margin', None))
        setattr(self, "_{}".format('opacity'), kwargs.get('opacity', None))
        setattr(self, "_{}".format('outline'), kwargs.get('outline', None))
        setattr(self, "_{}".format('outline_offset'), kwargs.get('outline_offset', None))
        setattr(self, "_{}".format('padding'), kwargs.get('padding', None))
        setattr(self, "_{}".format('width'), kwargs.get('width', None))

    @property
    def background_color(self):
        """Gets the background_color of this BaseAgreeButtonStyles.  # noqa: E501

        Control the background color of the element.  # noqa: E501

        :return: The background_color of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this BaseAgreeButtonStyles.

        Control the background color of the element.  # noqa: E501

        :param background_color: The background_color of this BaseAgreeButtonStyles.  # noqa: E501
        :type: str
        """

        self._background_color = background_color

    @property
    def border(self):
        """Gets the border of this BaseAgreeButtonStyles.  # noqa: E501

        Control the border of the element.  # noqa: E501

        :return: The border of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: str
        """
        return self._border

    @border.setter
    def border(self, border):
        """Sets the border of this BaseAgreeButtonStyles.

        Control the border of the element.  # noqa: E501

        :param border: The border of this BaseAgreeButtonStyles.  # noqa: E501
        :type: str
        """

        self._border = border

    @property
    def border_color(self):
        """Gets the border_color of this BaseAgreeButtonStyles.  # noqa: E501

        Control the border color of the element.  # noqa: E501

        :return: The border_color of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: str
        """
        return self._border_color

    @border_color.setter
    def border_color(self, border_color):
        """Sets the border_color of this BaseAgreeButtonStyles.

        Control the border color of the element.  # noqa: E501

        :param border_color: The border_color of this BaseAgreeButtonStyles.  # noqa: E501
        :type: str
        """

        self._border_color = border_color

    @property
    def border_radius(self):
        """Gets the border_radius of this BaseAgreeButtonStyles.  # noqa: E501

        Control the border radius of the element.  # noqa: E501

        :return: The border_radius of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: str
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, border_radius):
        """Sets the border_radius of this BaseAgreeButtonStyles.

        Control the border radius of the element.  # noqa: E501

        :param border_radius: The border_radius of this BaseAgreeButtonStyles.  # noqa: E501
        :type: str
        """

        self._border_radius = border_radius

    @property
    def border_style(self):
        """Gets the border_style of this BaseAgreeButtonStyles.  # noqa: E501

        Control the border style of the element.  # noqa: E501

        :return: The border_style of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: str
        """
        return self._border_style

    @border_style.setter
    def border_style(self, border_style):
        """Sets the border_style of this BaseAgreeButtonStyles.

        Control the border style of the element.  # noqa: E501

        :param border_style: The border_style of this BaseAgreeButtonStyles.  # noqa: E501
        :type: str
        """

        self._border_style = border_style

    @property
    def border_width(self):
        """Gets the border_width of this BaseAgreeButtonStyles.  # noqa: E501

        Control the border width of the element.  # noqa: E501

        :return: The border_width of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: str
        """
        return self._border_width

    @border_width.setter
    def border_width(self, border_width):
        """Sets the border_width of this BaseAgreeButtonStyles.

        Control the border width of the element.  # noqa: E501

        :param border_width: The border_width of this BaseAgreeButtonStyles.  # noqa: E501
        :type: str
        """

        self._border_width = border_width

    @property
    def box_shadow(self):
        """Gets the box_shadow of this BaseAgreeButtonStyles.  # noqa: E501

        Control the display of the box shadow of the agree button.  # noqa: E501

        :return: The box_shadow of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: str
        """
        return self._box_shadow

    @box_shadow.setter
    def box_shadow(self, box_shadow):
        """Sets the box_shadow of this BaseAgreeButtonStyles.

        Control the display of the box shadow of the agree button.  # noqa: E501

        :param box_shadow: The box_shadow of this BaseAgreeButtonStyles.  # noqa: E501
        :type: str
        """

        self._box_shadow = box_shadow

    @property
    def color(self):
        """Gets the color of this BaseAgreeButtonStyles.  # noqa: E501

        Control the fore-ground color of the element.  # noqa: E501

        :return: The color of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this BaseAgreeButtonStyles.

        Control the fore-ground color of the element.  # noqa: E501

        :param color: The color of this BaseAgreeButtonStyles.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def font_family(self):
        """Gets the font_family of this BaseAgreeButtonStyles.  # noqa: E501

        Control the font family of the text.  # noqa: E501

        :return: The font_family of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: str
        """
        return self._font_family

    @font_family.setter
    def font_family(self, font_family):
        """Sets the font_family of this BaseAgreeButtonStyles.

        Control the font family of the text.  # noqa: E501

        :param font_family: The font_family of this BaseAgreeButtonStyles.  # noqa: E501
        :type: str
        """

        self._font_family = font_family

    @property
    def font_size(self):
        """Gets the font_size of this BaseAgreeButtonStyles.  # noqa: E501

        Control the font size of the text.  # noqa: E501

        :return: The font_size of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: str
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this BaseAgreeButtonStyles.

        Control the font size of the text.  # noqa: E501

        :param font_size: The font_size of this BaseAgreeButtonStyles.  # noqa: E501
        :type: str
        """

        self._font_size = font_size

    @property
    def font_style(self):
        """Gets the font_style of this BaseAgreeButtonStyles.  # noqa: E501

        Control the font style of the text.  # noqa: E501

        :return: The font_style of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: str
        """
        return self._font_style

    @font_style.setter
    def font_style(self, font_style):
        """Sets the font_style of this BaseAgreeButtonStyles.

        Control the font style of the text.  # noqa: E501

        :param font_style: The font_style of this BaseAgreeButtonStyles.  # noqa: E501
        :type: str
        """

        self._font_style = font_style

    @property
    def font_weight(self):
        """Gets the font_weight of this BaseAgreeButtonStyles.  # noqa: E501

        Control the font weight of the text.  # noqa: E501

        :return: The font_weight of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: object
        """
        return self._font_weight

    @font_weight.setter
    def font_weight(self, font_weight):
        """Sets the font_weight of this BaseAgreeButtonStyles.

        Control the font weight of the text.  # noqa: E501

        :param font_weight: The font_weight of this BaseAgreeButtonStyles.  # noqa: E501
        :type: object
        """

        self._font_weight = font_weight

    @property
    def height(self):
        """Gets the height of this BaseAgreeButtonStyles.  # noqa: E501

        Control the height of the agree button.  # noqa: E501

        :return: The height of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this BaseAgreeButtonStyles.

        Control the height of the agree button.  # noqa: E501

        :param height: The height of this BaseAgreeButtonStyles.  # noqa: E501
        :type: str
        """

        self._height = height

    @property
    def margin(self):
        """Gets the margin of this BaseAgreeButtonStyles.  # noqa: E501

        Control the margin of the element.  # noqa: E501

        :return: The margin of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: str
        """
        return self._margin

    @margin.setter
    def margin(self, margin):
        """Sets the margin of this BaseAgreeButtonStyles.

        Control the margin of the element.  # noqa: E501

        :param margin: The margin of this BaseAgreeButtonStyles.  # noqa: E501
        :type: str
        """

        self._margin = margin

    @property
    def opacity(self):
        """Gets the opacity of this BaseAgreeButtonStyles.  # noqa: E501

        Control the opacity of the element  # noqa: E501

        :return: The opacity of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: str
        """
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        """Sets the opacity of this BaseAgreeButtonStyles.

        Control the opacity of the element  # noqa: E501

        :param opacity: The opacity of this BaseAgreeButtonStyles.  # noqa: E501
        :type: str
        """

        self._opacity = opacity

    @property
    def outline(self):
        """Gets the outline of this BaseAgreeButtonStyles.  # noqa: E501

        Control the outline of the element  # noqa: E501

        :return: The outline of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: str
        """
        return self._outline

    @outline.setter
    def outline(self, outline):
        """Sets the outline of this BaseAgreeButtonStyles.

        Control the outline of the element  # noqa: E501

        :param outline: The outline of this BaseAgreeButtonStyles.  # noqa: E501
        :type: str
        """

        self._outline = outline

    @property
    def outline_offset(self):
        """Gets the outline_offset of this BaseAgreeButtonStyles.  # noqa: E501

        Conrol the outline offset of the element  # noqa: E501

        :return: The outline_offset of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: str
        """
        return self._outline_offset

    @outline_offset.setter
    def outline_offset(self, outline_offset):
        """Sets the outline_offset of this BaseAgreeButtonStyles.

        Conrol the outline offset of the element  # noqa: E501

        :param outline_offset: The outline_offset of this BaseAgreeButtonStyles.  # noqa: E501
        :type: str
        """

        self._outline_offset = outline_offset

    @property
    def padding(self):
        """Gets the padding of this BaseAgreeButtonStyles.  # noqa: E501

        Control the padding of the element.  # noqa: E501

        :return: The padding of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: str
        """
        return self._padding

    @padding.setter
    def padding(self, padding):
        """Sets the padding of this BaseAgreeButtonStyles.

        Control the padding of the element.  # noqa: E501

        :param padding: The padding of this BaseAgreeButtonStyles.  # noqa: E501
        :type: str
        """

        self._padding = padding

    @property
    def width(self):
        """Gets the width of this BaseAgreeButtonStyles.  # noqa: E501

        Control the width of the agree button.  # noqa: E501

        :return: The width of this BaseAgreeButtonStyles.  # noqa: E501
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this BaseAgreeButtonStyles.

        Control the width of the agree button.  # noqa: E501

        :param width: The width of this BaseAgreeButtonStyles.  # noqa: E501
        :type: str
        """

        self._width = width

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
        if issubclass(BaseAgreeButtonStyles, dict):
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
        if not isinstance(other, BaseAgreeButtonStyles):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BaseAgreeButtonStyles):
            return True

        return self.to_dict() != other.to_dict()