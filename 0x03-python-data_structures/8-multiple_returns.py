#!/usr/bin/python3


def multiple_returns(sentence):
    """
    function returns a tuple with the length of a string and its
    first character.

    Args:
        sentence: string to return its first character and length.

    Return:
        Tuple with the length and the first character.
    """
    my_list = []
    my_list.append(len(sentence))
    if not sentence:
        my_list.append(None)
    else:
        my_list.append(sentence[0])
    return tuple(my_list)
