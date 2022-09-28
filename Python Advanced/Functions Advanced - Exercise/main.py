def palindrome(word, index):

    if index >= len(word) // 2:
        return f"{word} is a palindrome"

    first_letter = word[index]
    last_letter = word[-1 - index]

    if first_letter != last_letter:
        return f"{word} is not a palindrome"

    return palindrome(word, index + 1)
