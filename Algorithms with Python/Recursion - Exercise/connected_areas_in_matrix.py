class Areas:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size

    def __repr__(self):
        return f"at ({self.row}, {self.col}), size: {self.size}"


def is_outside(row, col, rows, cols) -> bool:
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return True
    return False


def connected_areas(row, col, rows, cols, matrix):
    if is_outside(row, col, rows, cols):
        return 0
    if matrix[row][col] != "-":
        return 0

    matrix[row][col] = "V"
    result = 1
    result += connected_areas(row, col + 1, rows, cols, matrix)
    result += connected_areas(row, col - 1, rows, cols, matrix)
    result += connected_areas(row + 1, col, rows, cols, matrix)
    result += connected_areas(row - 1, col, rows, cols, matrix)
    return result


rows = int(input())
cols = int(input())
matrix = [list(input()) for _ in range(rows)]
areas = []

for row in range(rows):
    for col in range(cols):
        size = connected_areas(row, col, rows, cols, matrix)
        if size > 0:
            areas.append(Areas(row, col, size))


print(f"Total areas found: {len(areas)}")
for i, area in enumerate(sorted(areas, key=lambda x: x.size, reverse=True)):
    print(f"Area #{i + 1} {area}")

"""
5
10
*--*---*--
*--*---*--
*--*****--
*--*---*--
*--*---*--
"""