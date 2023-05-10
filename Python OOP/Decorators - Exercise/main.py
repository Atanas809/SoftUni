def even_parameters(func):
    def wrapper(*args):
        for x in args:
            if not isinstance(x, int) or x % 2 != 0:
                return "Please use only even numbers!"

        result = func(*args)

        return result

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result
