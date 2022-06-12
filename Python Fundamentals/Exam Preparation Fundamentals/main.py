import re

data = input()
expression = r"(:{2}|\*{2})([A-Z][a-z]{2,})\1"
matches = re.finditer(expression, data)
valid_emojis = list()

for match in matches:
    valid = match.group(0)
    valid_emojis.append(valid)

nums = r"\d+"
numbers = re.findall(nums, data)
all_nums = ""

for x in numbers:
    all_nums += x

cool_threshold = 1
