# Test input:
"""
5
0K0K0
K000K
00K00
K000K
0K0K0
"""


def moves(row, col, size):

    possible_moves = [
        [row - 2, col - 1],
        [row - 2, col + 1],
