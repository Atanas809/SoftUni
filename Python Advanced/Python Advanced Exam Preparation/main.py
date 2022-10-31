from collections import deque


def extra_parameters(command, end_or_beginning, numbers, my_list):
    if command == "add" and end_or_beginning == "beginning":
        for num in numbers[::-1]:
            my_list.appendleft(num)
    elif command == "add" and end_or_beginning == "end":
        for num in numbers:
