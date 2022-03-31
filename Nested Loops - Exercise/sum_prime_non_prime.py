# Задача 3:
# command = input()
# prime_numbers_sum = 0
# non_prime_numbers_sum = 0
# while command != "stop":
#     current_number = int(command)
#     if current_number < 0:
#         print("Number is negative.")
#     else:
#         number_is_prime = True
#         for number in range(2, current_number):
#             if current_number % number == 0:
#                 number_is_prime = False
#                 break
#         if number_is_prime:
#             prime_numbers_sum += current_number
#         else:
#             non_prime_numbers_sum += current_number
#
#     command = input()
# print(f"Sum of all prime numbers is: {prime_numbers_sum}")
# print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")