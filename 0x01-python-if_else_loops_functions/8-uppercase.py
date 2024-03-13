#!/usr/bin/python3


def uppercase(str):
    """
    Function print string in uppercase.

    Args:
        str: string to be printed in upper.
    """
    for char in str:
        if 97 <= ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{:s}".format(char), end="")
    print("", end="\n")
