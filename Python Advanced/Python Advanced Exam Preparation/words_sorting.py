def words_sorting(*args):
    my_dict = dict()
    for word in args:
        my_dict[word] = sum([ord(x) for x in word])

    result = sum(my_dict.values())

    if result % 2 == 0:
        sorted_by_keys = sorted(my_dict.items(), key=lambda x: x[0])
        output = [f"{x} - {y}" for x, y in sorted_by_keys]
        return '\n'.join(output)
    else:
        sorted_by_values = sorted(my_dict.items(), key=lambda x: -x[1])
        output = [f"{x} - {y}" for x, y in sorted_by_values]
        return '\n'.join(output)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
