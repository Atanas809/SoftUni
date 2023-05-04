def cache(func):

    my_log = dict()

    def wrapper(number):
        wrapper.log = my_log

        if number not in my_log:
            my_log[number] = func(number)
        return my_log[number]

    return wrapper
