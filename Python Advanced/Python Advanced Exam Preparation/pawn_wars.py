# Test inputs:
"""
1.
- - - - - - b -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -


2.
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
b - - - - - - -
- w - - - - - -
- - - - - - - -

"""


def capture(black_row, black_col, white_row, white_col):
    if abs(black_row - white_row) == 1:
        return ("w", black_row, black_col)
    else:
        if abs(black_row - white_row) % 2 == 0:
            while True:
                white_row -= 1
                if abs(black_row - white_row) > 1:
                    black_row += 1
                else:
                    break

            return ("b", white_row, white_col)

        while True:
            if abs(black_row - white_row) > 1:
                white_row -= 1
                black_row += 1
            else:
                break

        return ("w", black_row, black_col)


def board_value(row, col):
    row_values = [str(x) for x in range(8, 0, -1)]
    col_values = ["a", "b", "c", "d", "e", "f", "g", "h"]

    return f"{col_values[col]}{row_values[row]}"


def who_wins(black_col, white_col, size):

    if size - (size - white_col) <= size - black_col - 1:
        return "w"

    return "b"


size = 8

board = [input().split() for _ in range(size)]

black_pawn_row, black_pawn_col = None, None
white_pawn_row, white_pawn_col = None, None

for row in range(size):
    if "b" or "w" in board[row]:
        for col in range(size):
            if board[row][col] == "b":
                black_pawn_row, black_pawn_col = (row, col)
            elif board[row][col] == "w":
                white_pawn_row, white_pawn_col = (row, col)

if abs(black_pawn_col - white_pawn_col) == 1:
    pawn, capture_row, capture_col = capture(black_pawn_row, black_pawn_col, white_pawn_row, white_pawn_col)

    if pawn == "w":
        print(f"Game over! White win, capture on {board_value(capture_row, capture_col)}.")
    elif pawn == "b":
        print(f"Game over! Black win, capture on {board_value(capture_row, capture_col)}.")

else:
    winning_pawn = who_wins(black_pawn_row, white_pawn_row, size)

    if winning_pawn == "w":
        winning_row, winning_col = (0, white_pawn_col)
        print(f"Game over! White pawn is promoted to a queen at {board_value(winning_row, winning_col)}.")
    elif winning_pawn == "b":
        winning_row, winning_col = (7, black_pawn_col)
        print(f"Game over! Black pawn is promoted to a queen at {board_value(winning_row, winning_col)}.")
