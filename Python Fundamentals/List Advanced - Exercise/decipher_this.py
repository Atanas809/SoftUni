import re

def decipher():
    secret_message = input().split()

    num_expression = r"[0-9]+"
    letters_expression = r"[a-zA-Z]+"

    message = list()

    for i in secret_message:

        number = re.findall(num_expression, x)
        letters = re.findall(letters_expression, x)

        current_num = int(number[0])
        current_letter = letters[0]

        if len(current_letter) > 1:
            current_letter = current_letter[-1] + current_letter[1:-1] + current_letter[0]

        output = chr(int(current_num)) + current_letter

        message.append(output)

    print(' '.join(message))

decipher()
