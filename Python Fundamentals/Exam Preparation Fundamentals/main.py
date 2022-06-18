def result(final_cars):
    for key, value in final_cars.items():
        print(f"{key} -> Mileage: {final_cars[key][0]} kms, Fuel in the tank: {final_cars[key][1]} lt.")

def output(my_dict):

    command = input().split(" : ")

    while command[0] != "Stop":

        if command[0] == "Drive":
            car = command[1]
            distance = int(command[2])
            fuel = int(command[3])

            if my_dict[car][1] < fuel:
                print("Not enough fuel to make that ride")
            else:
                my_dict[car][0] += distance
                my_dict[car][1] -= fuel

                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

                if my_dict[car][0] >= 100000:
                    del my_dict[car]
                    print(f"Time to sell the {car}!")

        elif command[0] == "Refuel":
            car = command[1]
            fuel = int(command[2])

            if my_dict[car][1] + fuel > 75:
                diff = abs(75 - my_dict[car][1])
                my_dict[car][1] = 75
                print(f"{car} refueled with {diff} liters")
