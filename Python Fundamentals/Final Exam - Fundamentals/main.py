text = input()

command = input().split()

while command[0] != "End":

    if command[0] == "Translate":
        char = command[1]
        replacer = command[2]
