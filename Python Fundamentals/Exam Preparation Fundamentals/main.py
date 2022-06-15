import re

text = input()
expression = r"([@|#])(?P<f_word>[a-zA-z]{3,})\1\1(?P<s_word>[a-zA-z]{3,})\1"
matches = re.finditer(expression, text)
valid = list()
mirror_words = list()

for match in matches:
    f_word = match.group("f_word")
    s_word = match.group("s_word")

    valid.append(f_word)
    valid.append(s_word)

    if f_word == s_word[::-1]:
        mirror_words.append(f_word)
        mirror_words.append(s_word)

if len(valid) != 0:
    print(f"{len(valid) // 2} word pairs found!")
else:
    print("No word pairs found!")

if len(mirror_words) != 0:
    print("The mirror words are:")
    for x in range(0, len(mirror_words), 2):
        if x + 1 == len(mirror_words) - 1:
            print(f"{mirror_words[x]} <=> {mirror_words[x + 1]}")
        else:
            print(f"{mirror_words[x]} <=> {mirror_words[x + 1]}", end = ", ")
else:
    print("No mirror words!")
