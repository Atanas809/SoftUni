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
        output.append(f"{x}:")
        for v in y:
            output.append(f"-{v}")

    return '\n'.join(output)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
