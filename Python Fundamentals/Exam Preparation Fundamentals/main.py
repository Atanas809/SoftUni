def result(final_cars):
    for key, value in final_cars.items():
        print(f"{key} -> Mileage: {final_cars[key][0]} kms, Fuel in the tank: {final_cars[key][1]} lt.")

def output(my_dict):

    command = input().split(" : ")

    while command[0] != "Stop":
