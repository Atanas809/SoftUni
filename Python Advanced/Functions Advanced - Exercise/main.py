def concatenate(*args, **kwargs):
    text = ''.join(args)

    for key, value in kwargs.items():
