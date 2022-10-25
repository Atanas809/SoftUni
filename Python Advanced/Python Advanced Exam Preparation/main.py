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


def successfully_filled(bombs):
    if bombs["Datura Bombs"] >= 3 and bombs["Cherry Bombs"] >= 3 and bombs["Smoke Decoy Bombs"] >= 3:
        return True

    return False


bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]

type_bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}
