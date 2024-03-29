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

    for n in range(row - 1):
        for m in range(column - 1):
            if is_equals(matrix, n, m):
                counter += 1

    return counter


rows, columns = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

result = square_matrices(matrix, rows, columns)

print(result)
