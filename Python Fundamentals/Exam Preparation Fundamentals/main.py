def result(my_dict):
    for key, value in my_dict.items():
        print(f"{key} -> Composer: {my_dict[key][0]}, Key: {my_dict[key][1]}")


def output(my_dict):

    command = input().split("|")
