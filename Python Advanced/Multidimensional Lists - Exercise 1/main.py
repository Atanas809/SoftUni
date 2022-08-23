# Test input:
"""
3
1, 2, 3
4, 5, 6
7, 8, 9
"""


def primary_diagonal(matrix):
    return [matrix[n][n] for n in range(len(matrix))]


def secondary_diagonal(matrix):
