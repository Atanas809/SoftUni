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
        paper_size[0], paper_size[-1] = paper_size[-1], paper_size[0]
        continue

    result = current_egg + current_paper

    if result <= box_size:
        boxes_made += 1

if boxes_made >= 1:
    print(f"Great! You filled {boxes_made} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if egg_size:
    print(f"Eggs left: {', '.join(str(x) for x in egg_size)}")
if paper_size:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_size)}")
