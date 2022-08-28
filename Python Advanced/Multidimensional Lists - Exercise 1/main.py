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
