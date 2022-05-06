# First way:

command = input()

while command != "end":
    rev_word = command[::-1]

    print(f"{command} = {rev_word}")

    command = input()
