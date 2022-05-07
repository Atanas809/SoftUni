banned_words = input().split(", ")

text = input()

for x in banned_words:
    text = text.replace(x, "*" * len(x))

print(text)
