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
        if valid_brackets[last_bracket] != x:
            condition = False
            break
    else:
        condition = False
        break
