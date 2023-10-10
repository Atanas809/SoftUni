# NOTE: In practice, this recursion should not be used here (instead use an iterative solution)

def calc_fac(n):
    if n == 1:
        return n
    return n * calc_fac(n - 1)


n = int(input())
print(calc_fac(n))
