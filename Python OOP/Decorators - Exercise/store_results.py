def store_results(func):
    default_file = "./results.txt"

    def wrapper(*args):
        result = func(*args)
