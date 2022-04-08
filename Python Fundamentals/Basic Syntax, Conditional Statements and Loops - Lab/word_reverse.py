word = input()
reversed_word = ""
for char in range(len(word) - 1, -1, -1):
    reversed_word += word[char]
print(reversed_word)
