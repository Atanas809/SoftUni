def words_sorting(*args):
    my_dict = dict()
    for word in args:
        my_dict[word] = sum([ord(x) for x in word])

    result = sum(my_dict.values())

    if result % 2 == 0:
        sorted_by_keys = sorted(my_dict.items(), key=lambda x: x[0])
