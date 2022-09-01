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
        "down": [row + 1, col],
        "right": [row, col + 1],
        "left": [row, col - 1],
    }

    for key, value in possible_moves.items():
        if key == direction:
            return value


size = int(input())

matrix = []
alice_row = 0
alice_col = 0
