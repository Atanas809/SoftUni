from collections import deque

# Test input:
"""
5, 25, 25, 115
5, 15, 25, 35
"""


def possible_bomb_craft(result):
    if result == 40 or result == 60 or result == 120:
        return True

    return False
