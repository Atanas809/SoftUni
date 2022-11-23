from collections import deque

egg_size = deque([int(x) for x in input().split(", ")])
paper_size = [int(x) for x in input().split(", ")]

box_size = 50
boxes_made = 0
