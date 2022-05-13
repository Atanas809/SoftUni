import re

numbers = input()

expression = r"(^|(?<=\s))(-)?([0]|[1-9][0-9]*)\.?([0-9]+)?($|(?=\s))"

matches = re.finditer(expression, numbers)
