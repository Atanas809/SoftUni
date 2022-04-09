first_word = input()
second_word = input()

for char in range(len(first_word)):
    if first_word[char] != second_word[char]:
        replacement = second_word[char]
        new_word = first_word[0:char] + replacement + first_word[char + 1:]
        first_word = new_word
        print(first_word)
