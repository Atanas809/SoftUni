from collections import deque


def is_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def stock_availability(*args):
    products = args[0]
    command = args[1]
    products_list = deque(products)
