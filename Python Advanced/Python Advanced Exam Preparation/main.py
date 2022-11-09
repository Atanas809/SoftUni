def words_sorting(*args):
    my_dict = dict()
    for word in args:
        my_dict[word] = sum([ord(x) for x in word])

    result = sum(my_dict.values())
