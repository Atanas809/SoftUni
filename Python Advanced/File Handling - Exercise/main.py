import os


def sorted_result(dictionary):
    sorting = sorted(dictionary.items(), key=lambda x: (x[0], x[1]))
    return sorting


path = "./"
result = dict()

for _, _, files in os.walk(path):
