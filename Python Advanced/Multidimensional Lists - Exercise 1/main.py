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
