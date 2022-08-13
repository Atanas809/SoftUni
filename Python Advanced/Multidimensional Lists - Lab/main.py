

def only_even_nums(even_matrix):
    return [int(x) for x in even_matrix if x % 2 == 0]


def matrix():
    rows = int(input())

    even_matrix = []

    for n in range(rows):
        my_list = [int(x) for x in input().split(", ")]
        even_matrix.append(only_even_nums(my_list))

    print(even_matrix)
