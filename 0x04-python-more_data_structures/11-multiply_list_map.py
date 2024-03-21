#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    """
    function returns a list with the values multiplied
    by a number without using ant loop.

    Args:
        my_list: list of integers.
        number: number to multiply by.

    Return:
        list with all values multiplied by number.
    """
    return list(map(lambda x: x * number, my_list))
