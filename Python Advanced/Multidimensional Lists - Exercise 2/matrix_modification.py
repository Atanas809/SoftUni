# Test input:
"""
3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END
"""


def is_valid_coordinates(row, col, matrix):

    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        return True


rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

while True:
    commands = input().split()

    if commands[0] == "END":
        break

    command = commands[0]
    row = int(commands[1])
    col = int(commands[2])
    value = int(commands[3])

    if is_valid_coordinates(row, col, matrix):
        if command == "Add":
            matrix[row][col] += value
        else:
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

for column in matrix:
    print(*column, sep=" ")
