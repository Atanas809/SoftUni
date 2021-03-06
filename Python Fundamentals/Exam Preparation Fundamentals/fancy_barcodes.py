import re

num = int(input())
expression = r"@(#)+(?P<valid>[A-Z][a-zA-Z0-9]{4,}[A-Z])@(#)+"

for _ in range(num):
    is_valid = False
    data = input()
    group = ""
    matches = re.finditer(expression, data)

    for match in matches:
        valid = match.group("valid")
        is_valid = True

        for x in valid:
            if x.isdigit()
                group += x

        if group != "":
            print(f"Product group: {group}")
        else:
            print(f"Product group: 00")

    if not is_valid:
        print("Invalid barcode")
