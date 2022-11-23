from collections import deque

egg_size = deque([int(x) for x in input().split(", ")])
paper_size = [int(x) for x in input().split(", ")]

box_size = 50
boxes_made = 0

while egg_size and paper_size:
    current_egg = egg_size.popleft()
    current_paper = paper_size.pop()

    if current_egg <= 0:
        paper_size.append(current_paper)
        continue

    elif current_egg == 13:
        paper_size.append(current_paper)
