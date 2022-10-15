from os.path import exists
from os import remove

# Test input:
"""
Create-file.txt
Add-file.txt-First Line
Add-file.txt-Second Line
Create-file.txt
Add-file.txt-First Line
Add-file.txt-Second Line
Replace-random.txt-Some-some
Replace-file.txt-First-1st
Replace-file.txt-Second-2nd
Delete-random.txt
Delete-file.txt
End
"""

while True:
    data = input().split("-")
    command = data[0]

    if command == "End":
        break

    file_name = data[1]

    if command == "Create":
        if not exists(file_name):
            with open(f"./{file_name}", "w") as text_file:
                pass
            continue
        file = open(f"./{file_name}", "r+")
        file.truncate()
        file.close()

    elif command == "Add":
        content = data[2]

        with open(f"./{file_name}", "a") as file:
            file.write(f"{content}\n")

    elif command == "Replace":
        old_string = data[2]
        new_string = data[3]

        if exists(file_name):
            with open(f"./{file_name}", "r") as new_file:
                data = new_file.read()
            with open(f"./{file_name}", "w") as new_file:
                data = data.replace(old_string, new_string)
                new_file.write(data)
        else:
            print("An error occurred")

    else:
        if exists(file_name):
            remove(file_name)
