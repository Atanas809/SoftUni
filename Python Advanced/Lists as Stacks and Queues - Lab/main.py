from collections import deque

water_quantity = int(input())

people = deque()

name = input()

while name != "Start":
    people.append(name)

    name = input()

command = input()

while command != "End":

    if command.startswith("refill "):
        water_quantity += int(command.split()[1])
