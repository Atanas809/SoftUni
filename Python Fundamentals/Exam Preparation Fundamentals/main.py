import re

data = input()
expression = r"(:{2}|\*{2})([A-Z][a-z]{2,})\1"
matches = re.finditer(expression, data)
