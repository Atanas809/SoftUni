first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])

counter = int(input())

for _ in range(counter):
    command = input().split()

    if command[0] == "Add":
        current_numbers = set([int(x) for x in command[2:]])
        if command[1] == "First":
            first = first.union(current_numbers)
        else:
            second = second.union(current_numbers)
    elif command[0] == "Remove":
        current_numbers = set([int(x) for x in command[2:]])
        if command[1] == "First":
            first = first.difference(current_numbers)
        else:
            second = second.difference(current_numbers)
    else:
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
