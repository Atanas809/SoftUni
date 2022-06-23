def result(my_dict):
    for key, value in my_dict.items():
        print(f"{key} -> Composer: {my_dict[key][0]}, Key: {my_dict[key][1]}")


def output(my_dict):

    command = input().split("|")

    while command[0] != "Stop":

        if command[0] == "Add":
            piece = command[1]
            composer = command[2]
            key = command[3]

            if piece not in my_dict.keys():
                my_dict[piece] = list()
                my_dict[piece].append(composer)
                my_dict[piece].append(key)
                print(f"{piece} by {composer} in {key} added to the collection!")
            else:
                print(f"{piece} is already in the collection!")

        elif command[0] == "Remove":
            piece = command[1]
