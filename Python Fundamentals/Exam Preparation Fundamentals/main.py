encrypted_message = input()

command = input().split("|")

while command[0] != "Decode":

    if command[0] == "Move":
        length = int(command[1])
