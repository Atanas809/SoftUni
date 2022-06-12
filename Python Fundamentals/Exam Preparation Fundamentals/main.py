import re

data = input()
expression = r"(:{2}|\*{2})([A-Z][a-z]{2,})\1"
matches = re.finditer(expression, data)
valid_emojis = list()

for match in matches:
    valid = match.group(0)
