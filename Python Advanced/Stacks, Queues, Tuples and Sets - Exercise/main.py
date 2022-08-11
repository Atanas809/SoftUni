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

    result = first + second
    result1 = second + first

    if result in main_colors or result in secondary_colors.keys():
        crafted_colors.append(result)
        continue
    elif result1 in main_colors or result1 in secondary_colors.keys():
        crafted_colors.append(result1)
        continue

    first = first[:-1]
    second = second[:-1]

    data.insert(len(data) // 2, first)
    data.insert(len(data) // 2, second)

for key, value in secondary_colors.items():
    if key in crafted_colors:
        if value[0] not in crafted_colors or value[1] not in crafted_colors:
            crafted_colors.remove(key)

print(crafted_colors)
