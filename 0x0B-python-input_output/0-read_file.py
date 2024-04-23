#!/usr/bin/python3
""" Read file """


def read_file(filename=""):
    """
    function that reads a text file and prints it.

    Args:
        filename: name of the file.
    """
    with open(filename) as my_file:
        print(my_file.read(), end="")
