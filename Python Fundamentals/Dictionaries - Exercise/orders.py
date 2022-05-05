def output(my_dict):

    for key, value in my_dict.items():

        total_price = value[0] * value[1]

        print(f"{key} -> {total_price:.2f}")

def orders():

    info = input().split()

    my_dict = dict()

    while info[0] != "buy":

        name = info[0]
        price = float(info[1])
        quantity = int(info[2])


        if name not in my_dict.keys():
            my_dict[name] = list()
            my_dict[name].append(price)
            my_dict[name].append(quantity)
        else:
            my_dict[name][1] += quantity
            my_dict[name][0] = price

        info = input().split()

    output(my_dict)

orders()
