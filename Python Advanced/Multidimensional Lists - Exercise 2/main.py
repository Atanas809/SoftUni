# Test input:
"""
3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END
"""


def is_valid_coordinates(row, col, matrix):

    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        return True


rows = int(input())
