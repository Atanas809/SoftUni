def output(key_materials, junk):

    for key, value in key_materials.items():
        print(f"{key}: {value}")

    for x, y in junk.items():
        print(f"{x}: {y}")

def legendary_item(key_materials):

    for key, value in key_materials.items():
        if key == "shards" and value >= 250:
            key_materials[key] -= 250
            print("Shadowmourne obtained!")
        elif key == "fragments" and value >= 250:
            key_materials[key] -= 250
            print("Valanyr obtained!")
        elif key == "motes" and value >= 250:
            key_materials[key] -= 250
            print("Dragonwrath obtained!")


def farming():

    items = input().split()

    key_materials = {"shards": 0, "fragments": 0, "motes": 0}

    junk_items = dict()

    while len(items) != 0:

        quantity = int(items[0])
        material = items[1].lower()

        if material in key_materials.keys():
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                break
        else:
            if material not in junk_items.keys():
                junk_items[material] = quantity
            else:
                junk_items[material] += quantity

        items.remove(items[0])
        items.remove(items[0])

        if len(items) == 0:
            items = input().split()

    legendary_item(key_materials)
    output(key_materials, junk_items)

farming()
