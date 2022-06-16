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
