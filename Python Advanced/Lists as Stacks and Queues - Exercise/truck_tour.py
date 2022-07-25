from collections import deque

number_of_pumps = int(input())

current_pumps = deque()

for _ in range(number_of_pumps):
    current_pumps.append(input().split())

for way in range(number_of_pumps):
    current_petrol = 0
    for petrol, distance in current_pumps:
        current_petrol = current_petrol + int(petrol) - int(distance)
        if current_petrol < 0:
            current_pumps.append(current_pumps.popleft())
            break
    else:
        print(way)
        break
