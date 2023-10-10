def calc_fib(n):
    if n <= 1:
        return 1
    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_iterative(n):
    n1 = 0
    n2 = 1
    result = 0
    for _ in range(n):
        result = n1 + n2
        n1, n2 = n2, result

    return result


num = int(input())
# print(calc_fib(num))
print(calc_fib_iterative(num))
