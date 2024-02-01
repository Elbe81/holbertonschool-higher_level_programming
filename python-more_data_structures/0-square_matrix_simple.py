#!/usr/bin/python3
"""
Module to compute the square value of all integers of a matrix.
"""


def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    Args:
        matrix (list of lists): 2-dimensional array.

    Returns:
        list of lists: New matrix with each value squared.
    """

    new_matrix = []

    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(num ** 2)
        new_matrix.append(new_row)

    return new_matrix


if __name__ == "__main__":
    square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)

