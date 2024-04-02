#!/usr/bin/python3
""" Square class """


class Square():
    """
    Class that defines a square.

    Attributes:
        size: size of the square.
    """
    def __init__(self, size=0):
        """
        initializes the square size.

        Args:
            size: size of the square.

        Raise:
            TypeError: if size is not int
            ValueError: if size is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
