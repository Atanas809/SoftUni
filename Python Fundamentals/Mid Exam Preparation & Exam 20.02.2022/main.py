numbers = list(map(int, input().split(" ")))

command = input().split(" ")

while command[0] != "end":
    if command[0] == "decrease":
        numbers = list(map(lambda x: x - 1, numbers))
        command = input().split(" ")
