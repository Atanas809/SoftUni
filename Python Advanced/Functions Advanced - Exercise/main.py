def palindrome(word, index):

    if index >= len(word) // 2:
        return f"{word} is a palindrome"

    first_letter = word[index]
    last_letter = word[-1 - index]
