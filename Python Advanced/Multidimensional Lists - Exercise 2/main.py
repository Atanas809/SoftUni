# Test input:
"""
5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left
"""


def moves(row, col, direction):

    possible_moves = {
        "up": [row - 1, col],
