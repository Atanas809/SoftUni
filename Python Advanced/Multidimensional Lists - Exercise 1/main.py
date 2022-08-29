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
