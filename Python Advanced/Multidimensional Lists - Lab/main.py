def is_biggest(matrix, row, column):
    result = [0] * 4

    for n in range(row - 1):
        for m in range(column - 1):
            current_result = matrix[n][m] + matrix[n][m + 1] + matrix[n + 1][m] + matrix[n + 1][m + 1]
            if current_result > sum(result):
                result[0] = matrix[n][m]
                result[1] = matrix[n][m + 1]
                result[2] = matrix[n + 1][m]
                result[3] = matrix[n + 1][m + 1]

    return result


rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for n in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

biggest = is_biggest(matrix, rows, columns)
