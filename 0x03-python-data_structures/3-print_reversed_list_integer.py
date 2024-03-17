#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """
    function prints all integers of a list in reverse order.

    Args:
        my_list: list to print in reverse.
    """
    for i in my_list.reverse():
        print("{:d}".format(i))
