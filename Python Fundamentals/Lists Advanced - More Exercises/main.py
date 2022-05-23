import re

def output(secret_message, take, skip):

    x = 0
    y = 0

    current_text = ""

    condition = True

    while condition:

        while x < len(take):
            current_text += secret_message[:take[x]]

