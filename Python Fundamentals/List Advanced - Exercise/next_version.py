software_version = input().split(".")

current_version = int(''.join(software_version))

new_version = current_version + 1

output = [x for x in str(new_version)]

print(f"{'.'.join(output)}")
