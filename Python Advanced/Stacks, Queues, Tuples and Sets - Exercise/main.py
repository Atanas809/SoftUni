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
        while len(result) > 1:
            first = result.popleft()
            second = result.popleft()
            result.appendleft(my_dict[x](first, second))
    else:
        result.append(int(x))
