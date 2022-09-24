def kwargs_length(**kwargs):
    return len(kwargs)


# Test input:
dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
