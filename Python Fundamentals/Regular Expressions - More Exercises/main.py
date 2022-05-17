import re

def output(my_dict):

    val_list = list(sorted(my_dict.values(), reverse=True))

    best_points = val_list[:3]

    best_results = list()

    for x in range(0, len(best_points)):
        current_name = [k for k, v in my_dict.items() if v == best_points[x]]

        best_results.append(current_name[0])
