# Test input:
"""
3
11 2 4
4 5 6
10 8 -12
"""


def primary_diagonal(matrix):
    return [matrix[n][n] for n in range(len(matrix))]


def secondary_diagonal(matrix):
    return [matrix[n][len(matrix) - n - 1] for n in range(len(matrix))]


rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

primary = sum(primary_diagonal(matrix))
