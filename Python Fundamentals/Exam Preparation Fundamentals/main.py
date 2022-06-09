activation_key = input()

command = input().split(">>>")

while command[0] != "Generate":

    if command[0] == "Contains":

        substring = command[1]

        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
