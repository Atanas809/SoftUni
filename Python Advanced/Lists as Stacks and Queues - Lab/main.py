# Задача 3:

from collections import deque

q = deque()

while True:
    command = input()

    if command == "Paid":
        while q:
