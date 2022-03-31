# Задача 5:
# number = int(input())
#
# for current_number in range(1111, 10000):
#     special_number_is_found = True
#     current_number_in_string = str(current_number)
#     for index, current_digit in enumerate(current_number_in_string):
#         if int(current_digit) == 0 or number % int(current_digit) != 0:
#             special_number_is_found = False
#             break
#         continue
#     if special_number_is_found:
#         print(current_number, end = " ")