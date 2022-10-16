import re
import string


def symbols_counter(current_line):
    punctuations = string.punctuation

    counter = 0

    for symbol in punctuations:
        if symbol in current_line:
            counter += current_line.count(symbol)

    return counter


def chars_counter(current_line):
    counter = re.findall(r"\w", current_line)

    return len(counter)


with open("./text.txt", "r") as text_file:
    for index, line in enumerate(text_file):
        count_chars = chars_counter(line)
