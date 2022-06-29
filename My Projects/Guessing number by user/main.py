import random


def game(x):

    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:

        guess = int(input("Make you guess here: "))

        if guess < random_number:
            print(f"Your number {guess} is too low. Try again with a high one!")

        elif guess > random_number:
            print(f"Your number {guess} is too high. Try again with a low one!")

    print("Congrats! You won.")


game(100)
