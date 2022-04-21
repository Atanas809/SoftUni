words = input().split()

searched_word = input()

palindromes = list()

for i in words:
    if i == i[::-1]:
        palindromes.append(i)

print(palindromes)
print(f"Found palindrome {words.count(searched_word)} times")

