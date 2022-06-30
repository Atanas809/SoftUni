import random


def who_wins(player1, player2):

    if (player1 == "r" and player2 == "s") or\
        (player1 == "s" and player2 == "p") or\
        (player1 == "p" and player2 == "r"):

        return True


def game():

    user = input("(R) for Rock"
                 "\n(P) for Paper"
                 "\n(S) for Scissors"
                 "\nMake your choice: ").lower()

    computer = random.choice(["R", "P", "S"]).lower()

    if user == computer:
        return "It's a tie!"
