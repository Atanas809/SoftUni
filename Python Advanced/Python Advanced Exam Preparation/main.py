from math import floor

# Test input:
"""
5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
left
right
right
up
up
right

"""


def move_to_opposite_side(row, col, size):

    if row < 0:
        row = size - 1
        return row, col
    elif row >= size:
        row = 0
        return row, col
    elif col < 0:
        col = size - 1
        return row, col
    elif col >= size:
        col = 0
        return row, col


def is_valid_move(next_row, next_col, size):

    if 0 <= next_row < size and 0 <= next_col < size:
        return True

    return False


def moves(row, col, direction):

    if direction == "up":
        return row - 1, col
    elif direction == "down":
        return row + 1, col
