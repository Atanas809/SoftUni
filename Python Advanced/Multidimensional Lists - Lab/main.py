

def only_even_nums(even_matrix):
    return [int(x) for x in even_matrix if x % 2 == 0]


def matrix():
    rows = int(input())

    even_matrix = []
