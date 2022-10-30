

vowels = deque(input().split())
consonants = input().split()

word_found = ""

my_dict = {
    0: "rose",
    1: "tulip",
    2: "lotus",
    3: "daffodil",
}

searched_words = ["rose", "tulip", "lotus", "daffodil"]

founded = False

while True:
    if founded:
        break

    if not vowels or not consonants:
        break

    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for index in range(len(searched_words)):
        if current_vowel in searched_words[index]:
            searched_words[index] = searched_words[index].replace(current_vowel, "")
        if current_consonant in searched_words[index]:
            searched_words[index] = searched_words[index].replace(current_consonant, "")
        if searched_words[index] == "":
            word_found = my_dict[index]
            founded = True
            break

if word_found:
    print(f"Word found: {word_found}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join([x for x in vowels])}")
if consonants:
    print(f"Consonants left: {' '.join([x for x in consonants])}")
