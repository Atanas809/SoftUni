from collections import deque

green_light = int(input())
free_window = int(input())

command = input()

cars = deque()
passed_cars = 0
hit_at = ""
car_crashed = ""
crashed = False

while command != "END":

    if crashed:
        break
    else:
        green_duration = green_light
        while green_duration > 0 and cars:
            current_car = cars.popleft()
            if len(current_car) <= green_duration + free_window:
                passed_cars += 1
            else:
                hit_at = current_car[green_duration + free_window]
                car_crashed = current_car
                crashed = True
                break
