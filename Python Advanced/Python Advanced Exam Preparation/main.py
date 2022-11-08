def start_spring(**kwargs):
    my_dict = dict()

    for key, value in kwargs.items():
        if value not in my_dict.keys():
            my_dict[value] = list()
        my_dict[value].append(key)

    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0])))

    result = dict()

    for k, v in sorted_dict.items():
        v = sorted(v)
        result[k] = v

    output = []

    for x, y in result.items():
