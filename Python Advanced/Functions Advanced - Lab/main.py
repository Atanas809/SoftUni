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
