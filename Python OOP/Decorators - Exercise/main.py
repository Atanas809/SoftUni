def logged(func):
    def wrapper(*args):
        result = ""

        func_result = func(*args)
        result += f"you called {func.__name__}{args}\n"
        result += f"it returned {func_result}"

        return result

    return wrapper

@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))
