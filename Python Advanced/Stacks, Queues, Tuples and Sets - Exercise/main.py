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
