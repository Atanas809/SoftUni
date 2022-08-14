# Test input:
"""
2
1, 2, 3
4, 5, 6
"""


def flattening_matrix(matrix):
    print([int(x) for row in matrix for x in row])


def my_matrix():
    rows = int(input())

    matrix = []

    for n in range(rows):
        my_list = [int(x) for x in input().split(", ")]
        matrix.append(my_list)

    flattening_matrix(matrix)


my_matrix()
