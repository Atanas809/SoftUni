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


def list_manipulator(*args):
    my_list = deque(args[0])
    command = args[1]
    end_or_beginning = args[2]
    if len(args) > 3:
        numbers = args[3:]
        extra_parameters(command, end_or_beginning, numbers, my_list)
    else:
        if end_or_beginning == "end":
            my_list.pop()
        elif end_or_beginning == "beginning":
            my_list.popleft()

    return list(my_list)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
