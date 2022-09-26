from collections import deque


def math_operations(*args, **kwargs):

    values = deque(args)
    index = 1

    while values:
        if index > 4:
            index = 1
            continue
