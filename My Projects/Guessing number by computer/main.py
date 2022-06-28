import random


def computer_guessing(x):

    low = 1
    high = x

    feedback = ""

    while feedback != "c" and low != high:

        guess = random.randint(low, high)

        feedback = input(f"{guess} is the correct secret number?"
                         f"\n(C) for correct"
                         f"\n(H) for too high"
                         f"\n(L) for too low"
                         f"\nMake your choice: ").lower()

        if feedback == "h":
            high = guess - 1

        elif feedback == "l":
            low = guess + 1

    print(f"You won the game!")
