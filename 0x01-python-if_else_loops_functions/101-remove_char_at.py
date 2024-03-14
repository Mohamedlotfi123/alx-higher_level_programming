#!/usr/bin/python3


def remove_char_at(str, n):
    """
    function that creates a copy of the string removing the
    character at the position n "the C index way".

    Args:
        str: string to copy and remove form.
        n: index to be removed.

    """
    s = ""
    for i in range(len(str)):
        if i == n:
            continue
        s = s + str[i]
    return s
