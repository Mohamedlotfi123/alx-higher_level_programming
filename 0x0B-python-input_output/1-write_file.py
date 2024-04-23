#!/usr/bin/python3
""" Write to a file """


def write_file(filename="", text=""):
    """
    function that writes a string to a text file and returns
    the number of characters written.

    Args:
        filename: the name of the file.
        text: string to be write to the file.

    Return:
        the number of the characters weitten.
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        num_of_char = my_file.write(text)

    return num_of_char
