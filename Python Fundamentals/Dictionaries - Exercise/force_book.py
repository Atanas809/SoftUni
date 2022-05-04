# Задача 11:

def output(my_dict):

    for key, value in my_dict.items():
        if len(value) != 0:
            print(f"Side: {key}, Members: {len(value)}")
            for x in value:
                print(f"! {x}")

def star_wars():

    command = input()

    my_dict = dict()
    current_users = list()

    while command != "Lumpawaroo":

        if "|" in command:
            info = command.split(" | ")

            force_side = info[0]
            force_user = info[1]

            if force_side not in my_dict.keys():
                my_dict[force_side] = list()
            if force_user not in current_users:
                my_dict[force_side].append(force_user)
                current_users.append(force_user)

        elif "->" in command:
            info = command.split(" -> ")

            force_user = info[0]
            force_side = info[1]

            if force_side not in my_dict.keys() and force_user not in current_users:
                my_dict[force_side] = list()
                my_dict[force_side].append(force_user)
                current_users.append(force_user)
            elif force_user not in current_users:
                my_dict[force_side].append(force_user)
                current_users.append(force_user)
            else:
                for key, value in my_dict.items():
                    if force_user in value:
                        my_dict[key].remove(force_user)

                if force_side not in my_dict.keys():
                    my_dict[force_side] = list()

                my_dict[force_side].append(force_user)

            print(f"{force_user} joins the {force_side} side!")

        command = input()

    output(my_dict)


star_wars()
