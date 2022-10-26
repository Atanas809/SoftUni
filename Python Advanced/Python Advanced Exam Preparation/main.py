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
        "horizontally_right": [
            [row, col + 1],
            [row, col + 2],
            [row, col + 3],
            [row, col + 4],
            [row, col + 5],
            [row, col + 6],
            [row, col + 7],
        ],
        "horizontally_left": [
            [row, col - 1],
            [row, col - 2],
            [row, col - 3],
            [row, col - 4],
            [row, col - 5],
            [row, col - 6],
            [row, col - 7],
        ],
        "main_diagonal_down": [
            [row + 1, col + 1],
            [row + 2, col + 2],
            [row + 3, col + 3],
            [row + 4, col + 4],
            [row + 5, col + 5],
            [row + 6, col + 6],
            [row + 7, col + 7],
        ],
        "main_diagonal_up": [
            [row - 1, col - 1],
            [row - 2, col - 2],
            [row - 3, col - 3],
            [row - 4, col - 4],
            [row - 5, col - 5],
            [row - 6, col - 6],
            [row - 7, col - 7],
        ],
        "secondary_diagonal_down": [
            [row + 1, col - 1],
            [row + 2, col - 2],
            [row + 3, col - 3],
            [row + 4, col - 4],
            [row + 5, col - 5],
            [row + 6, col - 6],
            [row + 7, col - 7],
        ],
        "secondary_diagonal_up": [
            [row - 1, col + 1],
            [row - 2, col + 2],
            [row - 3, col + 3],
            [row - 4, col + 4],
            [row - 5, col + 5],
            [row - 6, col + 6],
            [row - 7, col + 7],
        ]
    }

    valid_moves = dict()

    for key, value in possible_moves.items():
        for position in value:
            if is_valid_position(position, size):
                if key not in valid_moves.keys():
                    valid_moves[key] = []
                valid_moves[key].append(position)

    return get_board_values(valid_moves, board)
