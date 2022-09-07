def houses_around(next_row, next_col, matrix, presents_left, kids):

    possible_moves = [
        [next_row - 1, next_col],
        [next_row + 1, next_col],
        [next_row, next_col - 1],
        [next_row, next_col + 1],
    ]

    for row, col in possible_moves:
        if presents_left and kids:
