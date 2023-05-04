def cache(func):

    my_log = dict()

    def wrapper(number):
        wrapper.log = my_log
