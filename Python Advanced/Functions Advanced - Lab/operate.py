def operate(operator, *args):
    def add():
        return sum(args)

    def subtract():
        result = args[0]
        for x in args[1:]:
            result -= x

        return result

    def multiply():
        result = 1
        for x in args:
            result *= x

        return result

    def divide():
        result = args[0]
        for x in args[1:]:
            result /= x

        return result

    if operator == "+":
        return add()
    if operator == "-":
        return subtract()
    if operator == "*":
        return multiply()
    if operator == "/":
        return divide()


# Test inputs:
print(operate("+", 1, 2, 3))
print(operate("/", 3, 4, 9, 3))
