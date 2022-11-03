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
