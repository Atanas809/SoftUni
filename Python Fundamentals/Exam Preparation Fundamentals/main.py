message = input()
command = input().split(":|:")


while command[0] != "Reveal":

    if command[0] == "InsertSpace":
        index = int(command[1])
        l_side = message[:index]
        r_side = message[index:]
        message = l_side + " " + r_side

        print(message)

    elif command[0] == "Reverse":
        substring = command[1]

        if substring in message:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
            print(message)
