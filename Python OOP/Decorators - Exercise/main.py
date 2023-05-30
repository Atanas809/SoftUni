def logged(func):
    def wrapper(*args):
        result = ""

        func_result = func(*args)
        result += f"you called {func.__name__}{args}\n"
        result += f"it returned {func_result}"
