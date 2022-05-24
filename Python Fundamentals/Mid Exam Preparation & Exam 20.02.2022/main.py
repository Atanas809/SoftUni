numbers = list(map(int, input().split(" ")))

command = input().split(" ")

while command[0] != "end":
    if command[0] == "decrease":
        numbers = list(map(lambda x: x - 1, numbers))
        command = input().split(" ")
        continue
    index1 = int(command[1])
    index2 = int(command[2])

    if command[0] == "swap":
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
    elif command[0] == "multiply":
        numbers[index1] = numbers[index1] * numbers[index2]
