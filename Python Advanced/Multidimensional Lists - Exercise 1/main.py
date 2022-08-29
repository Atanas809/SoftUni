from collections import deque

# •	* - a regular position on the field
# •	e - the end of the route
# •	c - coal
# •	s - miner
# Test input:

"""
5
up right right up right
* * * c *
* * * e *
* * c * *
s * * c *
* * c * *
"""


def move_is_valid(miner_row, miner_column, size, command):
    possible_moves = {
        "up": [miner_row - 1, miner_column],
        "down": [miner_row + 1, miner_column],
        "left": [miner_row, miner_column - 1],
        "right": [miner_row, miner_column + 1]
    }

    valid_moves = {}

    for key, value in possible_moves.items():
        current_row = value[0]
        current_column = value[1]
        if 0 <= current_row < size and 0 <= current_column < size and key == command:
            valid_moves[key] = [current_row, current_column]
            return True


def is_coal(game_map):
    coal = 0

    for row in game_map:
        if "c" in row:
            counter = [x for x in row if x == "c"]
            coal += len(counter)

    return coal


def miner_position(game_map):
    result = []

    for n in game_map:
        if "s" in n:
            miner_row = game_map.index(n)
            miner_col = n.index("s")
            result.append([miner_row, miner_col])
            return result


size = int(input())

commands = deque(input().split())

game_map = []

for _ in range(size):
    game_map.append([x for x in input().split()])

position = miner_position(game_map)

miner_row = position[0][0]
miner_column = position[0][1]

coal_left = is_coal(game_map)
failed = False

while coal_left > 0 and commands:
    current_command = commands.popleft()

    if current_command == "up":
        if move_is_valid(miner_row, miner_column, size, current_command):
            symbol_at_position = game_map[miner_row - 1][miner_column]
            if symbol_at_position == "*":
                game_map[miner_row][miner_column] = "*"
            elif symbol_at_position == "c":
                coal_left -= 1
                game_map[miner_row][miner_column] = "*"
            else:
                print(f"Game over! ({miner_row - 1}, {miner_column})")
                failed = True
                break
            game_map[miner_row - 1][miner_column] = "s"
            miner_row = miner_row - 1

    elif current_command == "down":
        if move_is_valid(miner_row, miner_column, size, current_command):
            symbol_at_position = game_map[miner_row + 1][miner_column]
