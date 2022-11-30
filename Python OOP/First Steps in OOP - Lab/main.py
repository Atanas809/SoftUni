def print_rhombus(result):
    output = '\n'.join(row for row in result)

    return output


def create_rhombus(n, i):
    output = []

    spaces = " " * (n - i - 1)
    stars = "* " * (i + 1)
    output.append(spaces + stars)

    return output
