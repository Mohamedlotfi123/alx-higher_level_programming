#!/usr/bin/python3


def uppercase(str):
    """
    Function that prints a string in uppercase

    Args:
        str: string to be printed in uppercase
    """
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()
