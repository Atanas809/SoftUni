from collections import deque

number_of_pumps = int(input())

current_pumps = deque()

for _ in range(number_of_pumps):
    current_pumps.append(input().split())

for way in range(number_of_pumps):
    current_petrol = 0
