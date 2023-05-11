from time import time


def exec_time(func):
    def wrapper(*args):
        start = time()
        func(*args)
        end = time()
        execution_time = end - start
        return execution_time

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
