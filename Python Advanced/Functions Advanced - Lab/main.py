def sorting_cheeses(**kwargs):
    cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    for key, value in cheeses:
        result.append(key)
        result.extend(sorted(value, reverse=True))

    return '\n'.join([str(x) for x in result])


# Test inputs:
print(
    sorting_cheeses(
