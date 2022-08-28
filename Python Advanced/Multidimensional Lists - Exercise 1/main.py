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
