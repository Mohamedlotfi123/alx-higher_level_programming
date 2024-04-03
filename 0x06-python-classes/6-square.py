#!/usr/bin/python3
""" Square class """


class Square():
    """
    Class that defines a square.

    Attributes:
        size: size of the square.
        position: position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initializes the square size.

        Args:
            size: size of the square.
        """
        self.__size = size
        self.__position = position

    def area(self):
        """ returns the current square area """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Return:
            size: the size of a square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Setter method for the size attribute.

        Args:
            size: the new size of the square.

        Raise:
            TypeError: if size is not int
            ValueError: if size is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """
        prints in stdout the square with the character #,
        and empty line if size is 0.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                # if not self.__position[1] > 0:
                for i in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print("")

    @property
    def position(self):
        """
        Getter method for the position attribute

        Return:
            position value.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute

        Args:
            value: new value for the position.

        Raise:
            TypeError: if the position is not tuple of 2 positive integers.
        """
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[1]) != int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
