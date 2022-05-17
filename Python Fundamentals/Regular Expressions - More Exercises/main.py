import re

def output(my_dict):

    val_list = list(sorted(my_dict.values(), reverse=True))

    best_points = val_list[:3]

    best_results = list()

    for x in range(0, len(best_points)):
        current_name = [k for k, v in my_dict.items() if v == best_points[x]]

        best_results.append(current_name[0])

    print(f"""1st place: {best_results[0]}
2nd place: {best_results[1]}
3rd place: {best_results[2]}
""")

def points(data):

    digits = r"\d"

    matches = re.findall(digits, data)

    current_points = 0

    for point in matches:
        current_points += int(point)

    return current_points

def names(data):

    letters = r"[a-zA-Z]+"

    matches = re.findall(letters, data)

    current_name = ''.join(matches)

    return current_name
