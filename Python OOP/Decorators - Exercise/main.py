def tags(tag):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            return f"<{tag}>{result}</{tag}>"

        return wrapper

    return decorator
