import re

def output(my_dict):

    val_list = list(sorted(my_dict.values(), reverse=True))

    best_points = val_list[:3]

    best_results = list()
