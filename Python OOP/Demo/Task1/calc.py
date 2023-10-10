from validations import validate_operator
from functools import reduce


def get_result(first_num, second_num, operator):
    output = float('-inf')

    if operator == '+':
        my_list = [first_num, second_num]
        output = reduce(lambda x, y: x + y, my_list)
    elif operator == '-':
        my_list = [first_num, second_num]
        output = reduce(lambda x, y: x - y, my_list)
    elif operator == '*':
        my_list = [first_num, second_num]
        output = reduce(lambda x, y: x * y, my_list)
    elif operator == '/':
        my_list = [first_num, second_num]
        output = int(reduce(lambda x, y: x / y, my_list))

    return output


def calculator():
    print('-' * 30)
    first_num = int(input('Enter first number: '))
    second_num = int(input('Enter second number: '))
    operator = input('Enter operator: ')
    validate_operator(operator)

    result = get_result(first_num, second_num, operator)

    if result % 2 == 0:
        print(f'Result: {result} (Even)')
    else:
        print(f'Result: {result} (Odd)')
