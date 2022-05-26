number = input()

num = list(map(lambda x: int(x), number))

reverse = sorted(num, reverse=True)

output = list(map(str, reverse))

print("".join(output))
