def age_assignment(*args, **kwargs):
    result = []

    for name in args:
        start_with = name[0]
        age = kwargs[start_with]
        result.append(f"{name} is {age} years old.")

    return '\n'.join(sorted(result))


# Test inputs:
print(age_assignment("Peter", "George", G=26, P=19))
