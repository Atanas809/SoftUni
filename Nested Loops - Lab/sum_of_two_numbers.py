start = int(input())
final = int(input())
magic_number = int(input())
magic_number_is_found = False
count_combination = 0


for x1 in range(start, final + 1):
    for x2 in range(start, final + 1):
        count_combination += 1
        if x1 + x2 == magic_number:
            magic_number_is_found = True
            break
    if magic_number_is_found:
        break
if magic_number_is_found:
    print(f"Combination N:{count_combination} ({x1} + {x2} = {magic_number})")
else:
    print(f"{count_combination} combinations - neither equals {magic_number}")

