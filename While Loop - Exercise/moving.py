# Задача 7:
# width = int(input())
# length = int(input())
# height = int(input())
# no_more_space = False
# total_volume = width * length * height
# total_boxes = 0
# command = input()
# while command != "Done":
#     number_of_boxes = int(command)
#     total_boxes += number_of_boxes
#     if total_boxes > total_volume:
#         no_more_space = True
#         break
#     command = input()
# if no_more_space:
#     difference = abs(total_boxes - total_volume)
#     print(f"No more free space! You need {difference} Cubic meters more.")
# else:
#     difference = abs(total_boxes - total_volume)
#     print(f"{difference} Cubic meters left.")