number_of_computers = int(input())
average_rating = 0
sales = 0


for computer in range(1, number_of_computers + 1):
    current_number = int(input())
    rating = current_number % 10
    current_sales = current_number // 10
    if rating == 2:
        sales += current_sales * 0
        average_rating += rating
    if rating == 3:
        sales += current_sales * 0.5
        average_rating += rating
    if rating == 4:
        sales += current_sales * 0.7
        average_rating += rating
    if rating == 5:
        sales += current_sales * 0.85
        average_rating += rating
    if rating == 6:
        sales += current_sales * 1
        average_rating += rating
total_average_rating = average_rating / number_of_computers
print(f"{sales:.2f}")
print(f"{total_average_rating:.2f}")
