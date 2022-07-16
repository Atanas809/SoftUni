
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

