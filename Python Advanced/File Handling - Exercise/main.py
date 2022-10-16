import re
import string


def symbols_counter(current_line):
    punctuations = string.punctuation

    counter = 0

    for symbol in punctuations:
        if symbol in current_line:
            counter += current_line.count(symbol)

    return counter
