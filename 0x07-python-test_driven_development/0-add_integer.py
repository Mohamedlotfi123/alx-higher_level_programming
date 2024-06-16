#!/bin/usr/python3
""" Function that adds two integers. """


def add_integer(a, b=98):
    """
    function to add two integers.

    Args:
        a: first int
        b: second int

    Raise:
        TypeError: if 'a' or 'b' is not int or float.

    Return:
        the sum of the two integers.
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    elif type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
