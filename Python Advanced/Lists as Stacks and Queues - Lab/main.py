
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

