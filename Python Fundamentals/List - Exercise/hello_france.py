def output(profit, budget, all_prices):

    for x in all_prices:
        print(f"{x:.2f}", end = " ")

    print(f"\nProfit: {profit:.2f}")

    final_price = sum(all_prices) + budget

    if final_price >= 150:
        print("Hello, France!")
    else:
        print("Not enough money.")

def buying():
    items = input().split("|")

    budget = int(input())

    profit = 0

    all_prices = list()

    for x in items:
        info = x.split("->")

        product = info[0]
        price = float(info[1])

        condition = False

        if product == "Clothes":
            if price <= 50:
                condition = True

        elif product == "Shoes":
            if price <= 35:
                condition = True

        elif product == "Accessories":
            if price <= 20.50:
                condition = True

        if condition:
            if budget - price >= 0:
                budget -= price
                new_price = price + (price * 0.4)
                all_prices.append(new_price)
                profit += new_price - price

    output(profit, budget, all_prices)

buying()
