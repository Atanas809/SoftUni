names = sorted(input().split(", "))

print(sorted(names, key=len, reverse=True))
