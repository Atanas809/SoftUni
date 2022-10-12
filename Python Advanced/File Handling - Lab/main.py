import re

searched_words = ""

with open("./words.txt", "r") as words:
    for word in words:
        searched_words = word.split()

occurrences = dict()

with open("./input.txt", "r") as file:
    for line in file:
        current_words = re.findall(r"\b\S+\b", line.lower())
        for word in searched_words:
            if word in current_words:
                counter = current_words.count(word)
                if word not in occurrences.keys():
