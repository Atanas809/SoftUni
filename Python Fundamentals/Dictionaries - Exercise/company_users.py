# Задача 10:

def output(my_dict):

    for key, value in my_dict.items():

        print(key)

        for id in value:
            print(f"-- {id}")

def companies():

    command = input().split(" -> ")

    my_dict = dict()

    while command[0] != "End":

        name_of_company = command[0]
        employee_id = command[1]

        if name_of_company not in my_dict.keys():
            my_dict[name_of_company] = list()

        if employee_id not in my_dict[name_of_company]:
            my_dict[name_of_company].append(employee_id)

        command = input().split(" -> ")


    output(my_dict)

companies()
