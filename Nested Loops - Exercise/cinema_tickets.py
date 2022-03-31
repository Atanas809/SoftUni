# Задача 6:
# command = input()
# student_ticket = 0
# standard_ticket = 0
# kid_ticket = 0
# total_tickets = 0
# while command != "Finish":
#     movie_name = command
#     free_seats = int(input())
#     total_seats = free_seats
#     sold_tickets = 0
#     while free_seats > 0:
#         ticket_type = input()
#         if ticket_type == "End":
#             break
#         elif ticket_type == "standard":
#             standard_ticket += 1
#         elif ticket_type == "student":
#             student_ticket += 1
#         elif ticket_type == "kid":
#             kid_ticket += 1
#         sold_tickets += 1
#         free_seats -= 1
#         total_tickets += 1
#     print(f"{movie_name} - {sold_tickets / total_seats * 100:.2f}% full.")
#     command = input()
# print(f"Total tickets: {total_tickets}")
# print(f"{student_ticket / total_tickets * 100:.2f}% student tickets.")
# print(f"{standard_ticket / total_tickets * 100:.2f}% standard tickets.")
# print(f"{kid_ticket / total_tickets * 100:.2f}% kids tickets.")
#
