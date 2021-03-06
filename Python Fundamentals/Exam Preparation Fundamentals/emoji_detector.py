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

for n in all_nums:
    cool_threshold *= int(n)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")

for v in valid_emojis:
    cool = 0
    searched = v[2:-2]
    for ch in searched:
        cool += ord(ch)
    if cool >= cool_threshold:
        print(v)
