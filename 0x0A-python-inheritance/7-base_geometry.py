#!/usr/bin/python3
""" BaseGeometry Class """


class BaseGeometry:
    """ Class that define a Geometry. """

    def area(self):
        """ Empty method that raise exceptions """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that validate the value.

        Args:
            name: a string.
            value: any type variable.

        Raise:
            TypeError: if naem is not int, or
            ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
