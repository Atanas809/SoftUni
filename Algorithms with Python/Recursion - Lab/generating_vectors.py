def gen_vectors(index, vectors):
    if index > len(vectors) - 1:
        print(*vectors, sep="")
        return

    for num in range(2):
        vectors[index] = num
        gen_vectors(index + 1, vectors)


n = int(input())
vec = [None] * n
gen_vectors(0, vec)
