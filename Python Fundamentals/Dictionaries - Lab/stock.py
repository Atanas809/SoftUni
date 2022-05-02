def output(my_dict):

    searched_items = input().split()

    for i in searched_items:
        if i in my_dict.keys():
            print(f"We have {my_dict[i]} of {i} left")
        else:
            print(f"Sorry, we don't have {i}")

def stock():

    data = input().split()

    my_dict = dict()

    for i in range(0, len(data) - 1, 2):

        product = data[i]
        quantity = int(data[i + 1])

        my_dict[product] = quantity

    output(my_dict)

stock()
