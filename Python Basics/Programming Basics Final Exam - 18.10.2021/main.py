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
    command = input()
price_for_toys = count_toys * 5
price_for_sweaters = count_sweaters * 15

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {price_for_toys}")
