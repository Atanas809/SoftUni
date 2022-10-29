from collections import deque

# Test input:
"""
5, 6, 4, 16, 11, 5, 30, 2, 3, 27
1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22
"""


def enough_fireworks(fireworks):
    if fireworks["Palm firework"] >= 3 and fireworks["Willow firework"] >= 3 and fireworks["Crossette firework"] >= 3:
        return True

    return False

def firework_made(sum_values, fireworks):
    if sum_values % 3 == 0 and sum_values % 5 != 0:
        fireworks["Palm firework"] += 1
        return True
    elif sum_values % 3 != 0 and sum_values % 5 == 0:
        fireworks["Willow firework"] += 1
        return True
    elif sum_values % 3 == 0 and sum_values % 5 == 0:
        fireworks["Crossette firework"] += 1
        return True

    return False


def is_valid_value(power, effect):
    if power > 0 and effect > 0:
        return True


firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]
