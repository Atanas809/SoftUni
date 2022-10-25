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

while True:
    if not bomb_effects or not bomb_casings:
        break

    if successfully_filled(type_bombs):
        break

    current_bomb_effect = bomb_effects.popleft()
    current_bomb_casings = bomb_casings.pop()

    result = current_bomb_effect + current_bomb_casings

    if not possible_bomb_craft(result):
        current_bomb_casings -= 5
        bomb_casings.append(current_bomb_casings)
        bomb_effects.appendleft(current_bomb_effect)
        continue

    if result == 40:
        type_bombs["Datura Bombs"] += 1
    elif result == 60:
        type_bombs["Cherry Bombs"] += 1
    elif result == 120:
        type_bombs["Smoke Decoy Bombs"] += 1

if successfully_filled(type_bombs):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
