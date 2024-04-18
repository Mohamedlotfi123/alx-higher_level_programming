#!/usr/bin/python3
""" Square Class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that define a square

    Attributes:
        size: size of the square (height and width)
    """
    def __init__(self, size):
        """ initailization method """
        if not super().integer_validator("size", size):
            self.__size = size
        super().__init__(size, size)

    def area(self):
        """ function that return the area of the square. """
        return self.__size * self.__size

    def __str__(self):
        """ return the print for the class """
        return "[Square] {}/{}".format(self.__size, self.__size)
