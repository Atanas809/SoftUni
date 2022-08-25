# Test input:
"""
2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END
"""


def is_valid_coordinates(coordinates, current_row, current_column):

    for x in range(0, len(coordinates), 2):
        row = int(coordinates[x])
        col = int(coordinates[x + 1])
        if row < 0 or col < 0:
            return False
        elif row >= current_row and col >= current_column:
            return False

    return True


rows, columns = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([j for j in input().split()])
