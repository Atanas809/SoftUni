from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted_items = dict()

while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()

    if current_material == 0 and current_magic == 0:
        continue

    if current_magic == 0:
        materials.append(current_material)
        continue

    if current_material == 0:
        magic_level.appendleft(current_magic)
        continue

    result = current_magic * current_material

    if result < 0:
        result = current_magic + current_material
        materials.append(result)
        continue

    elif result in presents.keys():
        if presents[result] not in crafted_items.keys():
            crafted_items[presents[result]] = 1
        else:
            crafted_items[presents[result]] += 1
    else:
        materials.append(current_material + 15)

if ("Doll" in crafted_items.keys() and "Wooden train" in crafted_items.keys()) or \
        ("Teddy bear" in crafted_items.keys() and "Bicycle" in crafted_items.keys()):
