# Задача 5:

number = int(input())

even = list()
odd = list()
negative = list()
positive = list()

for _ in range(number):

    current_num = int(input())

    if current_num < 0:
        negative.append(current_num)
    else:
        positive.append(current_num)

    if current_num % 2 == 0:
        even.append(current_num)
    else:
        odd.append(current_num)

needed_list = input()

if needed_list == "even":
    print(even)
elif needed_list == "odd":
    print(odd)
elif needed_list == "positive":
    print(positive)
else:
    print(negative)