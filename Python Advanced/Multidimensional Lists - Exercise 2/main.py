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
        [row + 2, col + 1],
        [row + 2, col - 1],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row + 1, col - 2],
        [row + 1, col + 2]
    ]

    count = 0

    for knight_row, knight_col in possible_moves:
        if 0 <= knight_row < size and 0 <= knight_col < size and board[knight_row][knight_col] == "K":
            count += 1
    return count
