from collections import deque

# Test input:
"""
105 20 30 25
120 60 11 400 10 1
"""


def other_operations(material, magic, items, result):
    if result < 100:
        if result % 2 == 0:
            material *= 2
            magic *= 3
            final_result = material + magic
            valid_values(final_result, items)
        else:
            material *= 2
            magic *= 2
            final_result = material + magic
            valid_values(final_result, items)
    elif result > 499:
        material //= 2
        magic //= 2
        final_result = material + magic
        valid_values(final_result, items)


def valid_values(result, items):
    if 100 <= result <= 199:
        items["Gemstone"] += 1
    elif 200 <= result <= 299:
        items["Porcelain Sculpture"] += 1
    elif 300 <= result <= 399:
        items["Gold"] += 1
    elif 400 <= result <= 499:
        items["Diamond Jewellery"] += 1


materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

items = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while materials and magic_level:
    current_material = materials.pop()
    current_magic_level = magic_level.popleft()

    result = current_material + current_magic_level

    if 100 <= result <= 499:
        valid_values(result, items)
    else:
        other_operations(current_material, current_magic_level, items, result)

if (items["Gemstone"] >= 1 and items["Porcelain Sculpture"] >= 1) or\
    (items["Gold"] >= 1 and items["Diamond Jewellery"] >= 1):

    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

sorted_items = sorted(items.items(), key=lambda x: x[0])

for key, value in sorted_items:
    if value > 0:
        print(f"{key}: {value}")
