from words import words
import random
from visual_hangman import visual_lives


def valid_words():
    random_word = random.choice(words)

    while " " in random_word and "-" in random_word:
        random_word = random.choice(words)

    return random_word.upper()


def hangman():

    word = valid_words()
    letters_in_word = set(word)
    used_letters = set()
    lives = 6

    while len(letters_in_word) > 0 and lives > 0:

        print(f"{visual_lives[lives]}")
        secret_word = [x if x in used_letters else "_" for x in word]
        
        print(f"{' '.join(secret_word)}")
        print(f"You used these letters: {' '.join(used_letters)}")
        
        guess = input("Make your guess here: ").upper()

        if guess in letters_in_word:
            letters_in_word.remove(guess)

        elif guess in used_letters:
            print(f"\nYou already used letter {guess}")

        elif guess not in word:
            lives -= 1
            print(f"\nYour letter {guess} not in word")
            print(f"You have {lives} lives remaining")

        used_letters.add(guess)

    if len(letters_in_word) == 0:
        print(f"\nYou guess the secret word {word}")
    else:
        print(f"You've lost the game!")
        print(f"Your secret word was {word}")

        try_again = input("\nDo you want to try again with a new word?"
                          "\n            (Y) for YES"
                          "\n            (N) for NO"
                          "\nYour choice: ").upper()

        if try_again == "Y":
            hangman()


hangman()
