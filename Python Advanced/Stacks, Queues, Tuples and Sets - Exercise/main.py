from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

honey_made = 0

expressions = {
    "+": lambda a, b: a + b,
