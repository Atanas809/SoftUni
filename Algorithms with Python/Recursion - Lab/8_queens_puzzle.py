def print_board(board):
    for r in range(8):
        print(*board[r], sep=" ")
    print()


def can_place(row, col, rows, cols, left_diagonal, right_diagonal):
    if row in rows:
        return False
    if col in cols:
        return False
    if (col - row) in left_diagonal:
        return False
    if (col + row) in right_diagonal:
        return False

    return True


def place_queen(row, col, board, rows, cols, left_diagonal, right_diagonal):
    board[row][col] = "*"
    rows.add(row)
    cols.add(col)
    left_diagonal.add(col - row)
    right_diagonal.add(col + row)


def remove_queen(row, col, board, rows, cols, left_diagonal, right_diagonal):
    board[row][col] = "-"
    rows.remove(row)
    cols.remove(col)
    left_diagonal.remove(col - row)
    right_diagonal.remove(col + row)


def chess_board(row, board, rows, cols, left_diagonals, right_diagonals):
    if row == 8:
        print_board(board)
        return

    for c in range(8):
        if can_place(row, c, rows, cols, left_diagonals, right_diagonals):
            place_queen(row, c, board, rows, cols, left_diagonals, right_diagonals)
            chess_board(row + 1, board, rows, cols, left_diagonals, right_diagonals)
            remove_queen(row, c, board, rows, cols, left_diagonals, right_diagonals)


rows = 8
cols = 8
board = [["-" for _ in range(cols)] for _ in range(rows)]
chess_board(0, board, set(), set(), set(), set())
