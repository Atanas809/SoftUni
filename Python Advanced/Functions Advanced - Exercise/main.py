def even_odd_filter(**kwargs):
    new_dict = {}

    for key, value in kwargs.items():
        if key == "even":
            new_dict[key] = [x for x in value if x % 2 == 0]
