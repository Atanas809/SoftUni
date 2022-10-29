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
