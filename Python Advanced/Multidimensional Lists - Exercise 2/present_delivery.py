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
    elif current_dir == "left":
        return [row, col - 1]


present = int(input())

size = int(input())

matrix = []

santa_row = 0
santa_col = 0

nice_kids = 0

for current_row in range(size):
    column = input().split()
    for index in range(len(column)):
        if column[index] == "S":
            santa_row = current_row
            santa_col = index
        elif column[index] == "V":
            nice_kids += 1
    matrix.append(column)

happy_kids_left = nice_kids

while present:
    direction = input()

    if direction == "Christmas morning":
        break

    next_row, next_col = moves(santa_row, santa_col, direction)

    if is_valid_position(next_row, next_col, size):
        if matrix[next_row][next_col] == "V":
            present -= 1
            matrix[next_row][next_col] = "S"
            happy_kids_left -= 1
        elif matrix[next_row][next_col] == "X":
            matrix[next_row][next_col] = "S"
        elif matrix[next_row][next_col] == "C":

            present, happy_kids_left = houses_around(next_row, next_col, matrix, present, happy_kids_left)

            matrix[next_row][next_col] = "S"

            if not present or not happy_kids_left:
                matrix[santa_row][santa_col] = "-"
                break

        else:
            matrix[next_row][next_col] = "S"

        matrix[santa_row][santa_col] = "-"
        santa_row, santa_col = next_row, next_col

if not present and happy_kids_left:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row, sep=" ")

if not happy_kids_left:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
