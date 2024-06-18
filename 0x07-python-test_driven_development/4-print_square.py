#!/usr/bin/python3
""" print_square function """


def print_square(size):
    """
    function that prints a square with the character #.

    Args:
        size: the length of the square

    Raise:
        TypeError: if size is not int.
        ValueError: size must be >= 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        for _ in range(size):
            print('#', end="")
        print("")
