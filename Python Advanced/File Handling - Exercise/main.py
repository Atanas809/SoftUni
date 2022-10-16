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
        count_symbols = symbols_counter(line)
        with open("./output.txt", "a") as new_file:
            result = f"Line {index + 1}: {line} ({count_chars})({count_symbols})"
            new_file.write(f"{result}\n")
