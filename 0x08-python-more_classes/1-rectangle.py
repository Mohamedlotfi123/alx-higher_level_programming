#!/usr/bin/python3
""" Rectangel Class """


class Rectangle():
    """
    Class that defines a rectangle.

    Attributes:
        width: rectangle width
        height: rectangle height
    """
    def __init__(self, width=0, height=9):
        """ initailize instance attributes. """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Getter method for the width attribute. """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value: the new width for the rectangle.

        Raise:
            TypeError: if width is not int.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter method for the height attribute. """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value: the new height for the rectangle.

        Raise:
            TypeError: if height is not int.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
