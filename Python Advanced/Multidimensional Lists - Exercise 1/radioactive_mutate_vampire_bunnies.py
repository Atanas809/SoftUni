from collections import deque

# P - for player
# B - for bunnies
# . - for free space

# L - left
# R - right
# U - up
# D - down

# Test input:
"""
4 5
.....
.....
.B...
...P.
LLLLLLLL
"""


def is_dead(matrix, next_row, next_col):

    if matrix[next_row][next_col] == "B":
        return True


def bunny_spreading(matrix, bunnies, dead):

    new_bunnies = set()

    for bunny_row, bunny_col in bunnies:
        if 0 <= bunny_row - 1 < len(matrix) and 0 <= bunny_col < len(matrix[0]):
            if matrix[bunny_row - 1][bunny_col] == "P":
                dead = True
                matrix[bunny_row - 1][bunny_col] = "B"
                new_bunnies.add((bunny_row - 1, bunny_col))
            elif matrix[bunny_row - 1][bunny_col] != "B":
                matrix[bunny_row - 1][bunny_col] = "B"
                new_bunnies.add((bunny_row - 1, bunny_col))
        if 0 <= bunny_row + 1 < len(matrix) and 0 <= bunny_col < len(matrix[0]):
            if matrix[bunny_row + 1][bunny_col] == "P":
                dead = True
                matrix[bunny_row + 1][bunny_col] = "B"
                new_bunnies.add((bunny_row + 1, bunny_col))
            elif matrix[bunny_row + 1][bunny_col] != "B":
                matrix[bunny_row + 1][bunny_col] = "B"
                new_bunnies.add((bunny_row + 1, bunny_col))
        if 0 <= bunny_row < len(matrix) and 0 <= bunny_col - 1 < len(matrix[0]):
            if matrix[bunny_row][bunny_col - 1] == "P":
                dead = True
                matrix[bunny_row][bunny_col - 1] = "B"
                new_bunnies.add((bunny_row, bunny_col - 1))
            elif matrix[bunny_row][bunny_col - 1] != "B":
                matrix[bunny_row][bunny_col - 1] = "B"
                new_bunnies.add((bunny_row, bunny_col - 1))
        if 0 <= bunny_row < len(matrix) and 0 <= bunny_col + 1 < len(matrix[0]):
            if matrix[bunny_row][bunny_col + 1] == "P":
                dead = True
                matrix[bunny_row][bunny_col + 1] = "B"
                new_bunnies.add((bunny_row, bunny_col + 1))
            elif matrix[bunny_row][bunny_col + 1] != "B":
                matrix[bunny_row][bunny_col + 1] = "B"
                new_bunnies.add((bunny_row, bunny_col + 1))

    return (bunnies.union(new_bunnies), dead)


def moves(player_row, player_col, current_direction):
    possible_moves = {
        "U": lambda a, b: [a - 1, b],
        "D": lambda a, b: [a + 1, b],
        "L": lambda a, b: [a, b - 1],
        "R": lambda a, b: [a, b + 1]
    }

    return possible_moves[current_direction](player_row, player_col)


rows, columns = [int(x) for x in input().split()]

player_row = 0
player_col = 0

matrix = []

bunnies = set()

for row in range(rows):
    current_column = [x for x in input()]
    if "P" in current_column:
        player_row = row
        player_col = current_column.index("P")
    for bunny in range(len(current_column)):
        if current_column[bunny] == "B":
            bunnies.add((row, bunny))
    matrix.append(current_column)

commands = deque(input())

dead = False

while True:

    current_direction = commands.popleft()

    next_row, next_col = moves(player_row, player_col, current_direction)

    if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix[0]):
        if is_dead(matrix, next_row, next_col):
            matrix[player_row][player_col] = "."
            bunnies, dead = bunny_spreading(matrix, bunnies, dead)
            for row in matrix:
                print(*row, sep="")
            print(f"dead: {next_row} {next_col}")
            break
        else:
            matrix[player_row][player_col] = "."
            matrix[next_row][next_col] = "P"
            player_row, player_col = next_row, next_col
            bunnies, dead = bunny_spreading(matrix, bunnies, dead)
            if dead:
                for row in matrix:
                    print(*row, sep="")
                print(f"dead: {next_row} {next_col}")
                break

    else:
        matrix[player_row][player_col] = "."
        bunnies, dead = bunny_spreading(matrix, bunnies, dead)
        for row in matrix:
            print(*row, sep="")
        print(f"won: {player_row} {player_col}")
