from collections import deque


def best_list_pureness(*args):
    numbers = deque(args[0])
    counter = args[-1]
    best_pureness = float("-inf")
