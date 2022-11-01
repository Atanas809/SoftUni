from collections import deque


def best_list_pureness(*args):
    numbers = deque(args[0])
    counter = args[-1]
    best_pureness = float("-inf")
    best_index = 0
    for x in range(counter):
        current_pureness = 0
