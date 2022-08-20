# Test input:
"""
3 4
A B B D
E B B B
I J B B
"""


def is_equals(matrix, n, m):
    return matrix[n][m] == matrix[n][m + 1] == matrix[n + 1][m] == matrix[n + 1][m + 1]


def square_matrices(matrix, row, column):
    counter = 0
