import re

text = input()
expression = r"([@|#])(?P<f_word>[a-zA-z]{3,})\1\1(?P<s_word>[a-zA-z]{3,})\1"
matches = re.finditer(expression, text)
valid = list()
mirror_words = list()
