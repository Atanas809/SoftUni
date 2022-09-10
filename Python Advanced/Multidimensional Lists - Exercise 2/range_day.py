# Test input:
"""
. . . . .
x . . . .
. A . . .
. . . x .
. x . . x
3
shoot down
move right 4
move left 1
"""


def is_valid(next_row, next_col, size):
    return 0 <= next_row < size and 0 <= next_col < size


def moves(row, col, direction, step):
    if direction == "up":
        return [row - step, col]
    elif direction == "down":
        return [row + step, col]
    elif direction == "right":
        return [row, col + step]
    elif direction == "left":
        return [row, col - step]


size = 5

matrix = []

shooter_row = 0
shooter_col = 0
targets = 0
hit_targets = []

for rows in range(size):
    current_col = [x for x in input().split()]
    for cols in range(len(current_col)):
        if current_col[cols] == "A":
            shooter_row = rows
            shooter_col = cols
        elif current_col[cols] == "x":
            targets += 1
    matrix.append(current_col)

counter = int(input())

left_targets = targets
no_targets = False

for _ in range(counter):
    data = input().split()
    command = data[0]
    direction = data[1]

    if command == "move":
        steps = int(data[2])

        next_row, next_col = moves(shooter_row, shooter_col, direction, steps)

        if is_valid(next_row, next_col, size):
            if matrix[next_row][next_col] == ".":
                matrix[next_row][next_col] = "A"
                matrix[shooter_row][shooter_col] = "."
                shooter_row, shooter_col = next_row, next_col

    else:

        bullet_row, bullet_col = moves(shooter_row, shooter_col, direction, 1)

        while is_valid(bullet_row, bullet_col, size):
            if matrix[bullet_row][bullet_col] == "x":
                matrix[bullet_row][bullet_col] = "."
                left_targets -= 1
                hit_targets.append([bullet_row, bullet_col])
                break

            bullet_row, bullet_col = moves(bullet_row, bullet_col, direction, 1)

        if not left_targets:
            break

if left_targets:
    print(f"Training not completed! {left_targets} targets left.")
