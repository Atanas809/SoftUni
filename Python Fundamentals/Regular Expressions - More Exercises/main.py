import re

def race():

    participants = input().split(",")

    my_dict = dict()

    data = input()

    while data != "end of race":

        current_name = names(data)
        current_points = points(data)
