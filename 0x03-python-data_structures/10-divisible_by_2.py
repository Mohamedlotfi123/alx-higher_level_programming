#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """
    function find all multiples of 2 in a list.

    Args:
        my_list: list of integers.

    Return:
        new list of True and False. depending on whether the integer at
        the same position in my_list is a multiple of 2.
    """
    Is_multiple_of_2 = []
    for i in my_list:
        if i % 2 == 0:
            Is_multiple_of_2.append(True)
        else:
            Is_multiple_of_2.append(False)
    return Is_multiple_of_2
