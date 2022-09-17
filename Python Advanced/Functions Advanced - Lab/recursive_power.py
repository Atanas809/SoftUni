def recursive_power(number, power):
    if power == 0:
        return 1

    result = number * recursive_power(number, power - 1)

    return result


# Test inputs:
print(recursive_power(2, 10))
print(recursive_power(10, 100))
