number_of_rooms = int(input())

chairs_left = 0
condition = True

for x in range(1, number_of_rooms + 1):
    info = input().split()

    chairs = len(info[0])
    people = int(info[1])

    if chairs < people:
        diff = abs(chairs - people)
        print(f"{diff} more chairs needed in room {x}")
        condition = False
    else:
        free_chairs += abs(chairs - people)

if condition:
    print(f"Game On, {free_chairs} free chairs left")
