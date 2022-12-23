def read_next(*args):
    for x in args:
        for char in x:
            yield char
