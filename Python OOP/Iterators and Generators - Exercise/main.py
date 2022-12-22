def get_primes(obj):
    for x in obj:
        if x > 1:
            for i in range(2, x):
                if x % i == 0:
                    break
            else:
                yield x


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
