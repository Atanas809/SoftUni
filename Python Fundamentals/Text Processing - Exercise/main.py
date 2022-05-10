import string

def replacer():

    current_words = input().split()

    letters = string.ascii_lowercase

    final_result = 0

    for word in current_words:

        current_result = 0

        number = ""

        for n in range(0, len(word)):
            if word[n].isdigit():
                number += word[n]

        current_number = int(number)

        if word[0].isupper():
            letter_index = letters.index(word[0].lower()) + 1
            current_result += current_number / letter_index
        else:
            letter_index = letters.index(word[0].lower()) + 1
            current_result += current_number * letter_index

        if word[-1].isupper():
            letter_index = letters.index(word[-1].lower()) + 1
            current_result -= letter_index
        else:
            letter_index = letters.index(word[-1].lower()) + 1
            current_result += letter_index

        final_result += current_result

    print(f"{final_result:.2f}")

replacer()
