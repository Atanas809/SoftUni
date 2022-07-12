from collections import deque

kids = deque(input().split())

tosses = int(input())

current_toss = 0

while len(kids) > 1:
    current_toss += 1

    current_kid = kids.popleft()

    if current_toss < tosses:
        kids.append(current_kid)
    else:
        print(f"Removed {current_kid}")
        current_toss = 0

print(f"Last is {kids.pop()}")
