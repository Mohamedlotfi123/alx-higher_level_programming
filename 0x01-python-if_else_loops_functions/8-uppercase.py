#!/usr/bin/python3


def uppercase(str):
    """
    Function that prints a string in uppercase

    Args:
        str: string to be printed in uppercase
    """
    for i in str:

        # Check if the character is lower
        if ord(i) in range(97, 123):

            # convert it to upper:
            # "the difference between upper and lower in ASCII is 32"
            x = ord(i) - 32

        else:
            # if not lower don't change anything
            x = ord(i)

        #print("{}".format(chr(x)), end="")
    print()
