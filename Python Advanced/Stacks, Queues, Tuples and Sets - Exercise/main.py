from collections import deque

data = deque(input().split())

main_colors = ["red", "blue", "yellow"]

secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

crafted_colors = list()

while len(data) > 1:
    first = data.popleft()
    second = data.pop()
