# Test input:
"""
. . . . . . . .
Q . . . . . . .
. K . . . Q . .
. . Q Q . . . .
Q . . . Q . . .
. Q . . . . . .
. . . . . . Q .
. Q . Q . . . .
"""


def get_board_values(valid_moves, board):
    result = []
    for key, value in valid_moves.items():
