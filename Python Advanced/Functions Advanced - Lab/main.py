def multiply(*args):
    result = 1

    for num in args:
        result *= num

    return result


# Test input:
print(multiply(1, 4, 5))
