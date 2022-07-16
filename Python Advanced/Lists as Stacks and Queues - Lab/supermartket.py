# Задача 3:

from collections import deque

q = deque()

while True:
    command = input()

    if command == "Paid":
        while q:
            print(q.popleft())
    elif command == "End":
        print(f"{len(q)} people remaining.")
        break
    else:
        q.append(command)
