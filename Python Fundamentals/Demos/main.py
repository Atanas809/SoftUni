my_list = input().split("!")

command = input().split()

while command[0] != "Go":

    if command[0] == "Urgent":
        item = command[1]

    elif command[0] == "Unnecessary":
        item = command[1]
