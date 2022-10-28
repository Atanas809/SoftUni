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

    if len(args) > 2:
        if command == "delivery":
            items_to_be_delivered = args[2:]
