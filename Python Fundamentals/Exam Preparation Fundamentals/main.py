password = input()

command = input().split()

while command[0] != "Done":

    if command[0] == "TakeOdd":
        new_password = ""
        for x in range(1, len(password), 2):
            new_password += password[x]

        password = new_password
        print(password)

    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])

        text = password[index: index + length]

        password = password.replace(text, "", 1)

        print(password)

    else:
        old = command[1]
        new = command[2]

        if old in password:
            password = password.replace(old, new)
            print(password)
        else:
            print("Nothing to replace!")
