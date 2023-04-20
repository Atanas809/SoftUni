def number_increment(numbers):
    def increase():
        result = []
        for x in numbers:
            result.append(x + 1)

        return result

    return increase()
