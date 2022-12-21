def fibonacci():
    first_num = 0
    second_num = 1
    yield first_num
    yield second_num

    while True:
        result = first_num + second_num
        first_num, second_num = second_num, result
        yield result
