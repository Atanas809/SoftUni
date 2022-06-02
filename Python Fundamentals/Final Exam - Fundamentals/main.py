def output(my_dict):
    print(f"{len(my_dict.keys())} followers")

    for key, value in my_dict.items():
        print(f"{key}: {sum(value)}")

def social():

    command = input().split(": ")

    my_dict = dict()

    while command[0] != "Log out":

        if command[0] == "New follower":
            username = command[1]

            if username not in my_dict.keys():
                my_dict[username] = list()
                my_dict[username].append(0)
                my_dict[username].append(0)
