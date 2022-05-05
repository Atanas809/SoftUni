# Задача 7:

def output(parking):

    for key, value in parking.items():
        print(f"{key} => {value}")

def parking_lot():

    counter = int(input())

    parking = dict()

    for _ in range(counter):

        data = input().split()

        if data[0] == "register":

            name = data[1]
            car_plate = data[2]

            if name not in parking.keys():
                parking[name] = car_plate
                print(f"{name} registered {car_plate} successfully")
            else:
                print(f"ERROR: already registered with plate number {parking[name]}")

        elif data[0] == "unregister":

            name = data[1]

            if name in parking.keys():
                del parking[name]
                print(f"{name} unregistered successfully")
            else:
                print(f"ERROR: user {name} not found")

    output(parking)

parking_lot()
