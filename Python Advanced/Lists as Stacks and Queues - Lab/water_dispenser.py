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
    else:
        wanted_liters = int(command)
        person = people.popleft()

        if wanted_liters <= water_quantity:
            water_quantity -= wanted_liters
            print(f"{person} got water")
        else:
            print(f"{person} must wait")

    command = input()

print(f"{water_quantity} liters left")
