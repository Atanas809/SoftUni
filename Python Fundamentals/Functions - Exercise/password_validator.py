# Задача 9:
import re

def valid_digits(password):
    two_digits = False

    expression = r"(?P<two>[0-9]{2,})"

    matches = re.finditer(expression, password)

    for y in matches:
        two_digits = True
        break

    if not two_digits:
        return "Password must have at least 2 digits"
    else:
        return True

def valid_chars(password):
    no_special_chars = True

    special_chars = r"(?P<symbols>\W+)"

    special = re.finditer(special_chars, password)

    for x in special:
        no_special_chars = False
        break

    if not no_special_chars:
        print("Password must consist only of letters and digits")

def valid_length(password):

    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")

def valid():

    password = input()

    validator = False

    expression = r"^[a-zA-Z0-9]{6,10}$"

    is_valid = re.finditer(expression, password)

    for x in is_valid:
        if valid_digits(password) == True:
            validator = True
            print("Password is valid")
            break

    if not validator:
        valid_length(password)
        valid_chars(password)
        if valid_digits(password) != True:
            print(valid_digits(password))

valid()
