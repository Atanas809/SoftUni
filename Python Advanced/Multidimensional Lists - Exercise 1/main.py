# Test input:
"""
4
8 3 2 5
6 4 7 9
9 9 3 6
6 8 1 2
1,2 2,1 2,0
"""


def cells(matrix):
    return [x for row in matrix for x in row if x > 0]


def new_matrix(matrix, close_bombs, power):
    for row, column in close_bombs:
        matrix[row][column] -= power

    return matrix


def valid_bombs(matrix, row, column, size):
    possible_bombs = [
        [row - 1, column - 1],
        [row - 1, column],
        [row - 1, column + 1],
        [row, column - 1],
        [row, column + 1],
        [row + 1, column - 1],
        [row + 1, column],
        [row + 1, column + 1]
    ]

    bombs = []

    for current_row, current_column in possible_bombs:
        if 0 <= current_row < size and 0 <= current_column < size:
            if matrix[current_row][current_column] > 0:
                bombs.append([current_row, current_column])


size_matrix = int(input())

matrix = []

for _ in range(size_matrix):
    matrix.append([int(x) for x in input().split()])

bombs_indices = input().split()

for bomb in bombs_indices:
    row, column = [int(x) for x in bomb.split(",")]

    if matrix[row][column] > 0:
        close_bombs = valid_bombs(matrix, row, column, size_matrix)
