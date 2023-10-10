def reverse_array(idx, a, rev_a):
    if idx < 0:
        return
    rev_a.append(a[idx])
    reverse_array(idx - 1, a, rev_a)
    return rev_a


array = list(input().split(" "))
print(*reverse_array(len(array) - 1, array, []), sep=" ")
