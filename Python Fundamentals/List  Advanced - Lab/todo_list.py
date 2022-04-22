# Задача 3:
command = input().split("-")

todo_list = [" "] * 10

while command[0] != "End":

    index = int(command[0]) - 1
    note = command[1]

    todo_list[index] = note

    command = input().split("-")

while " " in todo_list:
    todo_list.remove(" ")

print(todo_list)
