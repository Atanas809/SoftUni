from collections import deque

# Test input:
"""
5 6
SoftUni
"""

rows, columns = [int(x) for x in input().split()]

text = deque(input())

matrix = []

for row in range(rows):
    snake = deque([])
    start, end, step = [0, columns, 1] if row % 2 == 0 else [columns - 1, -1, -1]
    for column in range(start, end, step):
        char = text.popleft()
        if end == -1:
            snake.appendleft(char)
        else:
            snake.append(char)
