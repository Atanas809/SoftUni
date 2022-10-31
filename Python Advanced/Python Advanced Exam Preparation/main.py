from collections import deque


def extra_parameters(command, end_or_beginning, numbers, my_list):
    if command == "add" and end_or_beginning == "beginning":
        for num in numbers[::-1]:
            my_list.appendleft(num)
    elif command == "add" and end_or_beginning == "end":
        for num in numbers:
            my_list.append(num)
    elif command == "remove" and end_or_beginning == "beginning":
        for _ in range(numbers[0]):
            my_list.popleft()
    elif command == "remove" and end_or_beginning == "end":
        for _ in range(numbers[0]):
            my_list.pop()
