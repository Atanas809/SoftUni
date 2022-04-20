def smallest_number():

    first_number = int(input())
    second_number = int(input())
    third_number = int(input())

    my_list = [first_number, second_number, third_number]

    smallest_number = min(my_list)

    return smallest_number

print(smallest_number())
