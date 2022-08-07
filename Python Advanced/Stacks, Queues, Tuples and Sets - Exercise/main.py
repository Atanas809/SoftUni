from collections import deque

expression = input().split()

result = deque()

my_dict = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b
}

for x in expression:
    if x in "-+*/":
