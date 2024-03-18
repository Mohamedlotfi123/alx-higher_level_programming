#!/usr/bin/python3


def max_integer(my_list=[]):
    """
    function finds the biggest integer of a list.

    Args:
        my_list: list of integers.

    Return:
        the biggest integer in my_list or,
        None if the list is empty.
    """
    biggest_int = 0
    if not my_list:
        return None
    for i in my_list:
        if i > biggest_int:
            biggest_int = i
    return biggest_int
