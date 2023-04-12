def multiply(times):
    def decorator(function):
        def wrapper(number):
            result = function(number)
            return result * times

        return wrapper

    return decorator
