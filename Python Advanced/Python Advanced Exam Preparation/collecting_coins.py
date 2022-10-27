from math import floor

# Test input:
"""
5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
left
right
right
up
up
right

"""


def move_to_opposite_side(row, col, size):

    if row < 0:
        row = size - 1
        return row, col
    elif row >= size:
        row = 0
        return row, col
    elif col < 0:
        col = size - 1
        return row, col
    elif col >= size:
        col = 0
        return row, col


def is_valid_move(next_row, next_col, size):

    if 0 <= next_row < size and 0 <= next_col < size:
        return True

    return False


def moves(row, col, direction):

    if direction == "up":
        return row - 1, col
    elif direction == "down":
        return row + 1, col
    elif direction == "left":
        return row, col - 1
    elif direction == "right":
        return row, col + 1


size = int(input())

field = []

player_row = None
player_col = None

for row in range(size):
    current_row_data = [x for x in input().split()]
    if "P" in current_row_data:
        for col in range(size):
            if current_row_data[col] == "P":
                player_row = row
                player_col = col
    field.append(current_row_data)

path = [[player_row, player_col]]

collected_coins = 0
valid_commands = ["up", "down", "left", "right"]
hit_a_wall = False

field[player_row][player_col] = "-"

while True:
    if collected_coins >= 100:
        break

    command = input()

    if command in valid_commands:
        next_row, next_col = moves(player_row, player_col, command)

        if is_valid_move(next_row, next_col, size):
            path.append([next_row, next_col])
            if field[next_row][next_col] == "X":
                hit_a_wall = True
                break
            elif field[next_row][next_col].isdigit():
                number = int(field[next_row][next_col])
                collected_coins += number
                field[next_row][next_col] = "0"
        else:
            next_row, next_col = move_to_opposite_side(next_row, next_col, size)
            path.append([next_row, next_col])
            if field[next_row][next_col] == "X":
                hit_a_wall = True
                break
            elif field[next_row][next_col].isdigit():
                number = int(field[next_row][next_col])
                collected_coins += number
                field[next_row][next_col] = "0"

        player_row, player_col = next_row, next_col

if hit_a_wall:
    collected_coins *= 0.5
    total_coins = floor(collected_coins)
    print(f"Game over! You've collected {total_coins} coins.")
else:
    print(f"You won! You've collected {collected_coins} coins.")

print("Your path:")
print(*path, sep="\n")
