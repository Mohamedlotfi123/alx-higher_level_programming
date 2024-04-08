#!/usr/bin/python3
""" Rectangel Class """


class Rectangle():
    """
    Class that defines a rectangle.

    Attributes:
        number_of_instances: the number of instance of the class
        width: rectangle width
        height: rectangle height
    """

    number_of_instances = 0

    def __init__(self, width=0, height=9):
        """ initailize instance attributes. """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ returns the area of the rectangel. """
        return self.__width * self.__height

    def perimeter(self):
        """ Return the rectangle perimeter. """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ print the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        rect += ("#" * self.__width + "\n") * (self.__height - 1)
        rect += "#" * self.__width
        return rect

    def __repr__(self):
        """ Return a string which can be parsed by the python interpreter. """
        s = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return s

    def __del__(self):
        """ print a message when delete an instance. """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
