# Задача 1:

text = input()

my_list = list()

for x in text:
    my_list.append(x)

my_stack = ""

while my_list:
    my_stack += (my_list.pop())

print(my_stack)
