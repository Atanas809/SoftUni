def type_check(types):
    def decorator(func):
        def wrapper(data):
            if not isinstance(data, types):
                return "Bad Type"

            return func(data)

        return wrapper

    return decorator
