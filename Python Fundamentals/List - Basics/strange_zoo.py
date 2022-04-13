# Задача 1:
tail = input()
body = input()
head = input()

my_list = [tail, body, head]

my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)

# Second way:

tail = input()
body = input()
head = input()

my_list = [tail, body, head]

my_list.reverse()

print(my_list)