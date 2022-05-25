
old_a = int(input())
old_b = int(input())

old = old_a, old_b

new = old_a, old_b = old_b, old_a

print(f"""Before:
a = {old[0]}
b = {old[1]}
