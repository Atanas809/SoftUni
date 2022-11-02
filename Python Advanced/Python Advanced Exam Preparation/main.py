def element_on_position(next_row, next_col, field):
    if field[next_row][next_col] == "R":
        return "R"
    elif field[next_row][next_col] == "W":
        return "W"
    elif field[next_row][next_col] == "M":
        return "M"
    elif field[next_row][next_col] == "C":
        return "C"


def opposite_side(next_row, next_col, size, field):
    if next_row < 0:
        return size - 1, next_col
    elif next_row == size:
        return 0, next_col
    elif next_col < 0:
        return next_row, size - 1
    elif next_col == size:
        return next_row, 0


def is_outside(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return False

    return True


def move(row, col, command):
    if command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col
    elif command == "left":
        return row, col - 1
    elif command == "right":
        return row, col + 1
