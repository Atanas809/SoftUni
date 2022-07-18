brackets = input()

stack = list()

valid_brackets = {
    "(": ")",
    "{": "}",
    "[": "]"
}

condition = True

for x in brackets:
    if x in "({[":
        stack.append(x)
    elif x in ")}]" and stack:
        last_bracket = stack.pop()
