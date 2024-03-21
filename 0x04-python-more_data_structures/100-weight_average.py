#!/usr/bin/python3


def weight_average(my_list=[]):
    """
    function returns the weighted average.

    Args:
        my_list: list of tuples.

    Return:
        weighted average.
    """
    if len(my_list) == 0:
        return 0
    t_of_weight = 0
    s = 0
    for t in my_list:
        score, weight = t
        s += score * weight
        t_of_weight += weight
    return s / t_of_weight
