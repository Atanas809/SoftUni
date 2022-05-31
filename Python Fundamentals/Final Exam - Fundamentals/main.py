text = input()

command = input().split()

while command[0] != "End":

    if command[0] == "Translate":
        char = command[1]
        replacer = command[2]

        text = text.replace(char, replacer)

        print(text)

    elif command[0] == "Includes":
        substring = command[1]

        if substring in text:
            print("True")
