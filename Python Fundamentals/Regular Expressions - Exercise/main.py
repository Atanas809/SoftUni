import re

expression = r"(^| )(?P<valid>([a-z0-9]+[-_.]*)+@([a-z]+[\-]?)+\.([a-z]+[\-]?)([\.]?[a-z]+[\-]?)?)\b"

info = input()

matches = re.finditer(expression, info)
