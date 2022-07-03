from words import words
import random
from visual_hangman import visual_lives


def valid_words():

    random_word = random.choice(words)

    while " " in random_word and "-" in random_word:
        random_word = random.choice(words)

    return random_word.upper()
