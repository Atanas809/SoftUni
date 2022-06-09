activation_key = input()
command = input().split(">>>")

while command[0] != "Generate":

    if command[0] == "Contains":

        substring = command[1]

        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command[0] == "Flip":
        start = int(command[2])
        end = int(command[3])
        if command[1] == "Upper":

            upper = activation_key[start:end].upper()
            activation_key = activation_key.replace(activation_key[start:end], upper)

        else:
            lower = activation_key[start:end].lower()
            activation_key = activation_key.replace(activation_key[start:end], lower)

        print(activation_key)

    else:
        start = int(command[1])
        end = int(command[2])

        need_to_remove = activation_key[start:end]
        activation_key = activation_key.replace(need_to_remove, "")

        print(activation_key)

    command = input().split(">>>")

print(f"Your activation key is: {activation_key}")
