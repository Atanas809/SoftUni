import re

def valid_users():

    usernames = input().split(", ")

    expression = r"^(?P<valid>[a-zA-Z0-9_-]{3,16})$"

    for x in usernames:
        matches = re.finditer(expression, x)

        for match in matches:
            print(match.group("valid"))

valid_users()
