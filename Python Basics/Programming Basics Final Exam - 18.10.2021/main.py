from math import floor

width = float(input())
length = float(input())
height = float(input())
average_astronauts_height = float(input())
spaceship_volume = width * length * height
room_volume = (average_astronauts_height + 0.4) * 4
total_astronauts = floor(spaceship_volume / room_volume)
