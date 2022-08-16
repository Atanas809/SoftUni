def is_biggest(matrix, row, column):
    result = [0] * 4

    for n in range(row - 1):
        for m in range(column - 1):
