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
