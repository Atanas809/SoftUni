def store_results(func):
    default_file = "./results.txt"

    def wrapper(*args):
        result = func(*args)
        with open(default_file, "a") as file:
            data = f"Function '{func.__name__}' was called. Result: {result}"
            file.write(data)
            file.write("\n")
