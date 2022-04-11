number_of_people = int(input())
capacity = int(input())

courses = 0
extra_courses = 0

while number_of_people != 0:
    if number_of_people >= capacity:
        number_of_people -= capacity
        courses += 1
    if number_of_people < capacity and number_of_people != 0:
        extra_courses += 1
        number_of_people = 0

all_courses = courses + extra_courses

print(all_courses)
