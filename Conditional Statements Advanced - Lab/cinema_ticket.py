# Задача 8:
day = input()
ticket_price = 0
if day == "Monday" or day == "Tuesday" or day == "Friday":
    ticket_price += 12
elif day == "Wednesday" or day == "Thursday":
    ticket_price += 14
else:
    ticket_price += 16

print(ticket_price)