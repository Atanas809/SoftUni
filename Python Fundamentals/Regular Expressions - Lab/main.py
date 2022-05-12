import re

names = input()

expression = r"\b([A-Z][a-z]+) ([A-Z][a-z]+)\b"

matches = re.finditer(expression, names)
