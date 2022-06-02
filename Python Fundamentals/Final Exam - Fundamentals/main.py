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
