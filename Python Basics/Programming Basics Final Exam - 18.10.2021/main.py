command = input()

adults = 0
kids = 0
count_toys = 0
count_sweaters = 0

while command != "Christmas":
    age = int(command)
    if age <= 16:
        kids += 1
        count_toys += 1
    else:
        adults += 1
        count_sweaters += 1
