def result(my_dict):
    for key, value in my_dict.items():
        print(f"{key}\n  HP: {my_dict[key][0]}\n  MP: {my_dict[key][1]}")
