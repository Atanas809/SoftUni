def next_question():
    print("\nLet's continue with you next question:")

    print("""Someone who strongly asserts a position is often said to be "putting his" what down?
A: Foot
B: Head
C: VCR remote
D: Money """)

    answer = "A"

    choice = input("You choice: ").upper()

    if answer == choice:
        print("\nCongratulation you won 10 000$")
    else:
        try_again()
            
def try_again():
    print("""\nYou lose!\nDo you want to restart the game?
    Type 'Y' for yes
    Type anything you want for EXIT
    """)

    y_n = input("Your choice: ").upper()

    if y_n == "Y":
        welcome()
    else:
        print("Have a nice day!")

def welcome():
    enter_name = input("Enter your name to continue playing the game: ")
    print(f"\nHello {enter_name}!\nWelcome to Become a millionaire game.")

    print("\nLet's start the game with your first question")

    question1 = input("""According to a well-known proverb, what do 'many hands make'?
 A: Light work
 B: Loud applause
 C: Many fingers
 D: Crowded mitten
""")

    answer = "A"

    your_answer = input("Make your choice.\nWhat answer do you picking?\nAnswer: ").upper()

    if your_answer == answer:
        print("\nAwesome you pick the right answer! Good job!")
        print("Do you want to continue with your next question?")
        print("""
    Type 'Y' for yes
    Type anything you want for EXIT       
""")
        choice = input("Your choice is? ").upper()

        if choice == "Y":
            print("Let's start!")
            next_question()

    else:
        print("Sorry but your answer is wrong!")
        try_again()

welcome()
