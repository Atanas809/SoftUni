# Задача 3:

def output(products):

    print("Products in stock:")

    for key, value in products.items():
        print(f"- {key}: {value}")

    print(f"Total Products: {len(products.keys())}")
    print(f"Total Quantity: {sum(products.values())}")

def statistic():

    command = input().split(": ")

    products = dict()

    while command[0] != "statistics":

        item = command[0]
        quantity = int(command[1])

        if item not in products.keys():
            products[item] = quantity
        else:
            products[item] += quantity

        command = input().split(": ")

    output(products)

statistic()
