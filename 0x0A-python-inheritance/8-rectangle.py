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
