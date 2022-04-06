number_of_floors = int(input())
number_of_rooms = int(input())
room_type = ""

for floors in range(number_of_floors, 0, -1):
    for rooms in range(number_of_rooms):
        if floors == number_of_floors:
            room_type = "L"
        elif floors % 2 == 0:
            room_type = "O"
        elif floors % 2 != 0:
            room_type = "A"
        print(f"{room_type}{floors}{rooms}", end = " ")

    print()
