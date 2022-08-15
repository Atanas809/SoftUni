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

    rows = int(input())

    matrix = []

    for n in range(rows):
        my_list = [int(x) for x in input().split()]
        matrix.append(my_list)

    primary_diagonal_sum(matrix)
