#!/usr/bin/python3
""" Rectangle Class. """
from . import base


class Rectangle(base.Base):
    """
    Rectangle class.

    Attributes:
        instance:
            __width: width of the rectangle
            __height: height of the rectangle
            __x: ...
            __y: ...
    Methods:
        Getter: for each attribute
        Setter: for eack attribute
        __init__: initialization method
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialization method

        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: ...
            y: ...
            id: id of the instance
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter for private attribute width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Setter for private attribute height
        """
        self.__width = width

    @property
    def height(self):
        """
        Getter for private attribute height.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Setter for private attribute height
        """
        self.__height = height

    @property
    def x(self):
        """
        Getter for private attribute x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Setter for private attribute x
        """
        self.__x = x

    @property
    def y(self):
        """
        Getter for private attribute y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Setter for private attraibute y
        """
        self.__y = y
