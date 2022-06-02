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

        elif command[0] == "Like":
            username = command[1]
            likes = int(command[2])

            if username not in my_dict.keys():
                my_dict[username] = list()
                my_dict[username].append(likes)
                my_dict[username].append(0)

            else:
                my_dict[username][0] += likes

        elif command[0] == "Comment":
            username = command[1]

            if username not in my_dict.keys():
                my_dict[username] = list()
                my_dict[username].append(0)
                my_dict[username].append(1)

            else:
                my_dict[username][1] += 1

        elif command[0] == "Blocked":

            username = command[1]

            if username not in my_dict.keys():
                print(f"{username} doesn't exist.")

            else:
                del my_dict[username]
