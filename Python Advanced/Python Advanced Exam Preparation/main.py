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
        current_count = {f"{key}": 0}
        for move in value:
            row = move[0]
            col = move[1]
            if current_count[key] == 0:
                if board[row][col] == "Q":
                    result.append(move)
                    current_count[key] += 1
            else:
                break

    return result
