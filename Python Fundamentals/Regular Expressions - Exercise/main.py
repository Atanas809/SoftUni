import re

expression = r"(?P<valid>(www\.([A-Za-z0-9\-]+)\.([\.a-z]+)+))"

data = input()

while data:

    matches = re.finditer(expression, data)
