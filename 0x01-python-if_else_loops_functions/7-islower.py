#!/usr/bin/python3


def islower(c):
    """
    Function that checks for lowercase character.

    Args:
        c: the character to check

    Return:
        True if c is lower, False if nor
    """
    if ord(c) in range(97, 123):
        return True
    else:
        return False
