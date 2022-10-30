
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
