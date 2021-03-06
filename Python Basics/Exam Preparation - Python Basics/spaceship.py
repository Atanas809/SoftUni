from math import floor

width = float(input())
length = float(input())
height = float(input())
average_astronauts_height = float(input())

spaceship_volume = width * length * height
room_volume = (average_astronauts_height + 0.4) * 4

total_astronauts = floor(spaceship_volume / room_volume)

if total_astronauts < 3:
    print("The spacecraft is too small.")
    
elif 3 <= total_astronauts <= 10:
    print(f"The spacecraft holds {total_astronauts} astronauts.")
    
else:
    print("The spacecraft is too big.")
