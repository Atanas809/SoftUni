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
