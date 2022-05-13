import re

dates = input()

expression = r"\b(?P<day>\d{2})([-.\/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"

matches = re.finditer(expression, dates)

for match in matches:
    day = match.group("day")
    month = match.group("month")
    year = match.group("year")
