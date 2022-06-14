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

        l_side = encrypted_message[:index]
        r_side = encrypted_message[index:]

        encrypted_message = l_side + value + r_side

    else:
        old = command[1]
        new = command[2]

        encrypted_message = encrypted_message.replace(old, new)

    command = input().split("|")

print(f"The decrypted message is: {encrypted_message}")
