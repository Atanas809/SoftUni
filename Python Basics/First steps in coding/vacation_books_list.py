# задача 4:
number_of_pages = int(input())
read_pages_for_hour = int(input())
number_of_days = int(input())

total_time = number_of_pages / read_pages_for_hour
needed_time = total_time / number_of_days

print(int(needed_time))

