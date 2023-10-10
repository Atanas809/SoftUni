def find_all_solutions(index, searched_word, words_indices, words_count, words):
    if index >= len(searched_word):
        print(*words, sep=" ")
        return
    if index not in words_indices:
        return

    for word in words_indices[index]:
        if words_count[word] == 0:
            continue
        words.append(word)
        words_count[word] -= 1

        find_all_solutions(index + len(word), searched_word, words_indices, words_count, words)
        words.pop()
        words_count[word] += 1


strings = input().split(", ")
searched_word = input()

words_indices = {}
words_count = {}

for s in strings:
    if s in words_count:
        words_count[s] += 1
        continue

    words_count[s] = 1

    try:
        index = 0
        while True:
            index = searched_word.index(s, index)

            if index not in words_indices:
                words_indices[index] = []
            words_indices[index].append(s)
            index += len(s)
    except ValueError:
        pass

find_all_solutions(0, searched_word, words_indices, words_count, [])

"""
Word, cruncher, cr, h, unch, c, r, un, ch, er
Wordcruncher
"""