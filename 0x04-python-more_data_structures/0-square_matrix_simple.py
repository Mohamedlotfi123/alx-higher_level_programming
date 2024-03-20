#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    function computes the square value of all integers of a matrix.

    Args:
        matitx: 2 dimensional array.

    Return:
        New matrix.
    """
    nmatrix = []
    for row in matrix:
        nrow = []
        for element in row:
            nrow.append(element ** 2)
        nmatrix.append(nrow)
    return nmatrix
