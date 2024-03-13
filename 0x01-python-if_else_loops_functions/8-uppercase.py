#!/usr/bin/python3


def uppercase(str):
    """
    Function that prints a string in uppercase

    Args:
        str: string to be printed in uppercase
    """
    for char in str:
        # Check if the character is lower
        if ord(char) in range(97, 123):
            # convert it to upper:
            # "the difference between upper and lower in ASCII is 32"
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()
