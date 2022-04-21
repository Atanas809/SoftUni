words = input().split()

searched_word = input()

palindromes = list()

for x in words:
    if x == x[::-1]:
        palindromes.append(x)

print(palindromes)
print(f"Found palindrome {words.count(searched_word)} times")

