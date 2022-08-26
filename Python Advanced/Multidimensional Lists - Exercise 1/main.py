# Test input:
"""
4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4
"""


def sum_values(result):

    total_sum = 0

    for row in result:
        total_sum += sum(row)

    return total_sum


def is_biggest(current_matrix):
    sum_matrix = 0

    for n in current_matrix:
        sum_matrix += sum(n)

    return sum_matrix


def new_matrix(matrix, row, column):
    return [
        [matrix[row][column], matrix[row][column + 1], matrix[row][column + 2]],
        [matrix[row + 1][column], matrix[row + 1][column + 1], matrix[row + 1][column + 2]],
        [matrix[row + 2][column], matrix[row + 2][column + 1], matrix[row + 2][column + 2]]
    ]


def biggest_sum(matrix, rows, columns):
    biggest = []
    sum_values = float("-inf")

    for row in range(rows - 2):
        for column in range(columns - 2):
            current_matrix = new_matrix(matrix, row, column)
            current_sum = is_biggest(current_matrix)
            if current_sum > sum_values:
                sum_values = current_sum
                biggest = current_matrix

    return biggest
