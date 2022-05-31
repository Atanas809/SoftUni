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
        else:
            print("False")

    elif command[0] == "Start":
        searched = command[1]

        length = len(searched) - 1

        if text[length + 1] == " " and text[: length + 1] == searched:
            print("True")
        else:
            print("False")

    elif command[0] == "Lowercase":

        text = text.lower()

        print(text)

    elif command[0] == "FindIndex":
        char = command[1]
