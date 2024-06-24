#!/usr/bin/python3
""" Square Class """
from . import rectangle


class Square(rectangle.Rectangle):
    """
    Square class.

    Attributes:
        instance:
            id: id of the instance
            width: width of the square
            height: height of the square
            x: position in the x axis
            y: position in the y axis
    Methods:
        __init__: initialization method.
        __str__: print [Square] (<id>) <x>/<y> - <size>
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initialization method for attributes.

        Args:
            size: the width and height of the square.
            x: position in the x axis
            y: position in the y axis
            id: if of the instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        function returns [Square] (<id>) <x>/<y> - <size>
        """
        to_print = f"({self.id}) {self.x}/{self.y} - {self.width}"
        return f"[Square] {to_print}"

    @property
    def size(self):
        """
        Getter for size attribute.

        Return:
            size attribute value.
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Setter for size attribute.
        """
        if type(size) is not int:
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = size
            self.height = size
