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


def is_valid_position(value, size):
    row = value[0]
    col = value[1]

    if 0 <= row < size and 0 <= col < size:
        return True

    return False

def moves(row, col, board, size):
    possible_moves = {
        "vertically_down": [
            [row + 1, col],
            [row + 2, col],
            [row + 3, col],
            [row + 4, col],
            [row + 5, col],
            [row + 6, col],
            [row + 7, col],
        ],
        "vertically_up": [
            [row - 1, col],
            [row - 2, col],
            [row - 3, col],
            [row - 4, col],
            [row - 5, col],
            [row - 6, col],
            [row - 7, col],
        ],
