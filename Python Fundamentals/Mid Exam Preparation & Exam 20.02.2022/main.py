
targets = list(map(int, input().split(" ")))

command = input().split(" ")

while command[0] != "End":
    index = int(command[1])
    value = int(command[2]
    if command[0] == "Shoot":
        if 0 <= index <= len(targets) - 1:
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
    elif command[0] == "Add":
        if 0 <= index <= len(targets) - 1:
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
