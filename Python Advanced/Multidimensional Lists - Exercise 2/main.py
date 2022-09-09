# Test input:
"""
. . . . .
x . . . .
. A . . .
. . . x .
. x . . x
3
shoot down
move right 4
move left 1
"""


def is_valid(next_row, next_col, size):
    return 0 <= next_row < size and 0 <= next_col < size


def moves(row, col, direction, step):
