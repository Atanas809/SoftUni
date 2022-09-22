def func_executor(*args):

    result = []

    for func_ref, func_arg in args:
        func_name = func_ref.__name__
        func_result = func_ref(*func_arg)
        result.append(f"{func_name} - {func_result}")

    return '\n'.join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


# Test input:
print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
