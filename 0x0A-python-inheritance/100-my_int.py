#!/usr/bin/python3
""" MyInt class """


class MyInt(int):
    """ Class that inherits from int class """
    def __init__(self, num):
        """ initailization method """
        self.first = num

    def __eq__(self, second):
        """
        customize the equal operation.

        Args:
            second: operand in the comparison

        Return:
            True if Not equal, or
            False if equal
        """
        if self.first != second:
            return True
        return False

    def __ne__(self, second):
        """
        customize the not equal operation.

        Args:
            second: operand in the comparison

        Return:
            True if equal, or
            False if Not equal
        """
        if self.first == second:
            return True
        return False
