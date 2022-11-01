from collections import deque


def best_list_pureness(*args):
    numbers = deque(args[0])
    counter = args[-1]
    best_pureness = float("-inf")
    best_index = 0
    for x in range(counter):
        current_pureness = 0
        for index, value in enumerate(numbers):
            current_pureness += index * value

        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_index = x

        numbers.appendleft(numbers.pop())

    return f"Best pureness {best_pureness} after {best_index} rotations"
