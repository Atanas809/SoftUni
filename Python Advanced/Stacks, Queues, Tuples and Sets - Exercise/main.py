from collections import deque

expression = input().split()

result = deque()

my_dict = {
    "+": lambda a, b: a + b,
