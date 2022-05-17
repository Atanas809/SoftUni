import re

def race():

    participants = input().split(",")

    my_dict = dict()

    data = input()

    while data != "end of race":

        current_name = names(data)
        current_points = points(data)

        for name in participants:

            if current_name == name.strip():
                if current_name not in my_dict.keys():
   
