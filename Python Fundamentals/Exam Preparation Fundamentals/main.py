import re

data = input()

expression = r"(=|\/)(?P<valid>[A-Z][a-zA-Z]{2,})\1"
