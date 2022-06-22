stops = input()
command = input().split(":")

while command[0] != "Travel":

    if command[0] == "Add Stop":
        index = int(command[1])
        text = command[2]
