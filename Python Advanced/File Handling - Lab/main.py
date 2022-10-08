file = open("./numbers.txt", "r")
sum_numbers = 0

for line in file:
    number = int(line)
    sum_numbers += number

print(sum_numbers)
