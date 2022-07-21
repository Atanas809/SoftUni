from collections import deque

food_quantity = int(input())

orders = deque(int(x) for x in input().split())

print(max(orders))
