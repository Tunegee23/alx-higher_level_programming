#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Square each element of matrix
    Args:
    matrix - a 2 dimensional lists"""

    if matrix is None:
        return None
    return [
            [x**2 for x in row] for row in matrix]
