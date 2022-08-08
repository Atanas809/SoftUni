first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])

counter = int(input())

for _ in range(counter):
    command = input().split()

    if command[0] == "Add":
        current_numbers = set([int(x) for x in command[2:]])
