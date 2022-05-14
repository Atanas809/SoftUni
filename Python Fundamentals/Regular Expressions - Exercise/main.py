import re

data = input()

expression = r"\b(?P<valid>_[A-Za-z0-9]+)\b"

for match in matches:
    valid = match.group("valid")[1:]
