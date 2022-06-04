my_list = input().split("!")

command = input().split()

while command[0] != "Go":

    if command[0] == "Urgent":
        item = command[1]

    elif command[0] == "Unnecessary":
        item = command[1]

        if item in my_list:
            my_list.remove(item)

    elif command[0] == "Correct":
        old = command[1]
        new = command[2]
