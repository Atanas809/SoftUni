def start_spring(**kwargs):
    my_dict = dict()

    for key, value in kwargs.items():
        if value not in my_dict.keys():
            my_dict[value] = list()
        my_dict[value].append(key)
