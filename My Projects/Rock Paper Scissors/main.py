import random


def who_wins(player1, player2):

    if (player1 == "r" and player2 == "s") or\
        (player1 == "s" and player2 == "p") or\
        (player1 == "p" and player2 == "r"):

        return True
