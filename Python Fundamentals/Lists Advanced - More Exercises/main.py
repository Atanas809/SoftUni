import re

def output(secret_message, take, skip):

    x = 0
    y = 0

    current_text = ""

    condition = True

    while condition:

        while x < len(take):
            current_text += secret_message[:take[x]]

            secret_message = secret_message.replace(secret_message[:take[x]], "", 1)

            x += 1

            break

        while y < len(skip):

            secret_message = secret_message[skip[y]:]

            y += 1

            break

        if x == len(take) and y == len(skip):
            condition = False

