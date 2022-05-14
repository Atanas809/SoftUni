import re

data = input()

output = list()

while data:

    matches = re.findall(r"\d+", data)

    for match in matches:

        output.append(match)

    data = input()

print(' '.join(output))
