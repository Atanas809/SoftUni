def output(my_dict):
    print(f"{len(my_dict.keys())} followers")

    for key, value in my_dict.items():
        print(f"{key}: {sum(value)}")
