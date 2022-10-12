import re

searched_words = ""

with open("./words.txt", "r") as words:
    for word in words:
        searched_words = word.split()
