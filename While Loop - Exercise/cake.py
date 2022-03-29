# Задача 6:
width = int(input())
length = int(input())
is_done = False
total_volume = width * length
number_of_pieces = 0

command = input()
while command != "STOP":
    current_pieces = int(command)
    number_of_pieces += current_pieces
    if number_of_pieces > total_volume:
        is_done = True
        break
    command = input()
if is_done:
    difference = abs(total_volume - number_of_pieces)
    print(f"No more cake left! You need {difference} pieces more.")
else:
    difference = total_volume - number_of_pieces
    print(f"{difference} pieces are left.")
