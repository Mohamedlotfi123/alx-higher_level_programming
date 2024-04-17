#!/usr/bin/python3
""" Rctangle Class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class that define Rectangle

    Attributes:
        width: width of the rectangel
        height: height of the rectangle
    """
    def __init__(self, width, height):
        """ initailization method """
        self.__width = width
        if not super().integer_validator("height", height):
            self.__height = height

    def area(self):
        """ return the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ implement the print of the class """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
