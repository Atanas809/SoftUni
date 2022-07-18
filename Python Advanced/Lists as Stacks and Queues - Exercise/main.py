brackets = input()

stack = list()

valid_brackets = {
    "(": ")",
    "{": "}",
    "[": "]"
}

condition = True

for x in brackets:
