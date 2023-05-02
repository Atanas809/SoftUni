def make_bold(func):
    def wrapper(*args):
        return f"<b>{func(*args)}</b>"

    return wrapper
