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
