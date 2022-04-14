# Задача 8:
def output(all_values, effort):

    print("Cells:")

    for x in all_values:
        print(f"- {x}")

    print(f"Effort: {effort:.2f}")
    print(f"Total Fire: {sum(all_values)}")

def fire():
    cells = input().split("#")

    water = int(input())

    effort = 0
    all_values = list()

    for x in cells:

        info = x.split(" = ")

        type_of_fire = info[0]
        value_of_cell = int(info[1])

        condition = False

        if type_of_fire == "High":
            if 81 <= value_of_cell <= 125:
                condition = True

        elif type_of_fire == "Medium":
            if 51 <= value_of_cell <= 80:
                condition = True

        elif type_of_fire == "Low":
            if 1 <= value_of_cell <= 50:
                condition = True

        if condition:
            if water - value_of_cell >= 0:
                water -= value_of_cell
                effort += value_of_cell * 0.25
                all_values.append(value_of_cell)

    output(all_values, effort)

fire()
