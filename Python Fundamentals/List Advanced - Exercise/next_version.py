# Задача 2:

version = input().split(".")

current_version = int(''.join(version))

new_version = current_version + 1

output = [x for x in str(new_version)]

print(f"{'.'.join(output)}")
