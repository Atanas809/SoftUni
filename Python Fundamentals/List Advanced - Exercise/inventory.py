def inventory():

    items = input().split(", ")

    command = input().split(" - ")

    while command[0] != "Craft!":

        if command[0] == "Collect":
            current_item = command[1]

            if current_item not in items:
                items.append(current_item)

        elif command[0] == "Drop":
            current_item = command[1]

            if current_item in items:
                items.remove(current_item)

        elif command[0] == "Combine Items":
            info = command[1].split(":")
            old_item = info[0]
            new_item = info[1]

            if old_item in items:
                index_old = items.index(old_item)

                items.insert(index_old + 1, new_item)

        elif command[0] == "Renew":

            current_item = command[1]

            if current_item in items:
                items.remove(current_item)
                items.append(current_item)


        command = input().split(" - ")

    print(', '.join(items))

inventory()
