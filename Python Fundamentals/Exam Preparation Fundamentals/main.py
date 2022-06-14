encrypted_message = input()

command = input().split("|")

while command[0] != "Decode":

    if command[0] == "Move":
        length = int(command[1])

        text = encrypted_message[:length]

        encrypted_message = encrypted_message.replace(text, "", 1)
        encrypted_message += text

    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
