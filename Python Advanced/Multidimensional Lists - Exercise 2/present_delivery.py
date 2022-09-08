def houses_around(next_row, next_col, matrix, presents_left, kids):

    possible_moves = [
        [next_row - 1, next_col],
        [next_row + 1, next_col],
        [next_row, next_col - 1],
        [next_row, next_col + 1],
    ]

    for row, col in possible_moves:
        if presents_left and kids:
            if matrix[row][col] == "V":
                kids -= 1
                presents_left -= 1
                matrix[row][col] = "-"
            elif matrix[row][col] == "X":
                matrix[row][col] = "-"
                presents_left -= 1
        else:
            return presents_left, kids

    return presents_left, kids


def is_valid_position(next_row, next_col, size):
    return 0 <= next_row < size and 0 <= next_col < size


def moves(row, col, current_dir):
    if current_dir == "up":
        return [row - 1, col]
    elif current_dir == "down":
        return [row + 1, col]
    elif current_dir == "right":
        return [row, col + 1]
