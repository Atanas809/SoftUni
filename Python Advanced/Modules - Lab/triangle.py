from packages.triangle_loop import print_triangle


def triangle(n):
    for i in range(n):
        print_triangle(i)

    for i in range(n - 2, -1, -1):
        print_triangle(i)


size = int(input())
triangle(size)
