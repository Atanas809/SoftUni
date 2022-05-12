import re

phones = input()

expression = r"\+359([ |-])2\1([0-9]{3})\1([0-9]{4})\b"

matches = re.finditer(expression, phones)

valid_phones = list()

for match in matches:
    valid_phones.append(match[0])
