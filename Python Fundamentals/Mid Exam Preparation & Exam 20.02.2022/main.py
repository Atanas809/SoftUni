
text = input()

indices = list()

for x in range(len(text)):
    if text[x].isupper():
        indices.append(x)
