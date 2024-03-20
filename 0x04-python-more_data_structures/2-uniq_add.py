#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    function adds all unique integers in a list.

    Args:
        my_list: list of integers.

    Return:
        sum of unique integers.
    """
    s = 0
    uniq_list = list(set(my_list))
    for number in uniq_list:
        s += number
    return s
