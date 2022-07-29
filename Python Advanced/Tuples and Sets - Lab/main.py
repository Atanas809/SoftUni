

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

def race():

    participants = input().split(",")

    my_dict = dict()

    data = input()

    while data != "end of race":

        current_name = names(data)
        current_points = points(data)

        for name in participants:

            if current_name == name.strip():
                if current_name not in my_dict.keys():
                    my_dict[current_name] = current_points
                else:
                    my_dict[current_name] += current_points

        data = input()

    output(my_dict)

race()

