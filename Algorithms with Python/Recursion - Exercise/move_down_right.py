def possible_paths(row, col, rows, cols, target):
    if row >= rows or col >= cols:
        return 0
    if (row, col) == target:
        return 1

    result = 0
    result += possible_paths(row + 1, col, rows, cols, target)
    result += possible_paths(row, col + 1, rows, cols, target)
    return result


rows = int(input())
cols = int(input())
target = (rows - 1, cols - 1)
print(possible_paths(0, 0, rows, cols, target))
