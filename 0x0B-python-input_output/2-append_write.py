#!/usr/bin/python3
""" Apprnd to a file """


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file and
    returns the number of characters added.

    Args:
        filename: name of the file.
        text: string to append to a file

    Return:
        Number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        num_of_char = my_file.write(text)

    return num_of_char
