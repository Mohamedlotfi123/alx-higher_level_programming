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
        __init__: initialization method
        Getter: for each attribute
        Setter: for eack attribute
        area: return the area of the rectangle
        display: prints the rectangle
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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
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
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
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
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
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
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        function return the area of a rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        function prints the rectangle using #
        """
        print(self.y * "\n", end="")
        for _ in range(self.__height):
            print(self.x * " ", end="")
            for _ in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """
        function returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        to_print = f"({self.id}) {self.x}/{self.y}"
        return f"[Rectangle] {to_print} - {self.width}/{self.height}"
