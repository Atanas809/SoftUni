def recursive_power(number, power):

    if power == 0:
        return 1

    result = number * recursive_power(number, power - 1)

    return result
