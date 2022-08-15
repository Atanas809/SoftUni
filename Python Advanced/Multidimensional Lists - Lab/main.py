# Test input:
"""
3
11 2 4
4 5 6
10 8 -12
"""


def primary_diagonal_sum(matrix):

    result = 0

    for n in range(len(matrix)):
        result += matrix[n][n]

    print(result)


def my_matrix():
