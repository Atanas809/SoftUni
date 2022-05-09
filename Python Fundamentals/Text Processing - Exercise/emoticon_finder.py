text = input()

while ":" in text:
    index = text.index(":")

    print(text[index] + text[index + 1])

    text = text.replace(":", "", 1)
