#!/usr/bin/python3
""" text_indentation function. """


def text_indentation(text):
    """
    function that prints two new lines after "." , ":" , "?"

    Args:
        text: text to print.

    Raise:
        TypeError: if text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    n_line = 0
    for char in text:
        if char in [".", ":", "?"]:
            print(char, "\n")
            n_line = 1
        elif n_line == 1 and char == " ":
            continue
        else:
            print(char, end="")
            n_line = 0
