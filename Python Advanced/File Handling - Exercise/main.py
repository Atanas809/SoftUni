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
