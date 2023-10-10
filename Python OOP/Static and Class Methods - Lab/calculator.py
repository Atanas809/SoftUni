from functools import reduce


class Calculator:

    @staticmethod
    def add(*args):
        return reduce(lambda x, y: x + y, args)
    # [1, 2, 3, 4]
    # (((1 + 2) + 3) + 4) = 10

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)
    # [1, 2, 3, 4]
    # (((1 * 2) * 3) * 4) = 24

    @staticmethod
    def divide(*args):
        return reduce(lambda x, y: x / y, args)
    # [1, 2, 3, 4]
    # (((1 / 2) / 3) / 4) = 0.04

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)
    # [1, 2, 3, 4]
    # (((1 - 2) - 3) - 4) = -8


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
