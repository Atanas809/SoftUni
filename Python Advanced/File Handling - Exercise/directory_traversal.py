import os


def sorted_result(dictionary):
    sorting = sorted(dictionary.items(), key=lambda x: (x[0], x[1]))
    return sorting


path = "./"
result = dict()

for _, _, files in os.walk(path):
    for file in files:
        extension = file.split(".")[-1]
        if extension not in result.keys():
            result[extension] = []
        result[extension].append(file)

result = sorted_result(result)

with open("./report.txt", "w") as new_file:
    for key, value in result:
        new_file.write(f".{key}\n")
        for file in value:
            new_file.write(f"- - - {file}\n")
