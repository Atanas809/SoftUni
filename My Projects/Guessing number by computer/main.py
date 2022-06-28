import random


def computer_guessing(x):

    low = 1
    high = x

    feedback = ""

    while feedback != "c" and low != high:
