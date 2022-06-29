import random


def game(x):

    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:

        guess = int(input("Make you guess here: "))
