stops = input()
command = input().split(":")

while command[0] != "Travel":

    if command[0] == "Add Stop":
        index = int(command[1])
        text = command[2]

        if 0 <= index <= len(stops) - 1:
            l_side = stops[:index]
            r_side = stops[index:]
            stops = l_side + text + r_side

        print(stops)

    elif command[0] == "Remove Stop":
        start = int(command[1])
        end = int(command[2])
        diff = abs(start - end)

        if 0 <= start + diff <= len(stops) - 1:
            text = stops[start: end + 1]
            stops = stops.replace(text, "")

        print(stops)

    else:
        old = command[1]
        new = command[2]

        if old in stops:
            stops = stops.replace(old, new)

        print(stops)
