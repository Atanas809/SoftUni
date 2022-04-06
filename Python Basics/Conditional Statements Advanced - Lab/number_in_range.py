# Finding numbers in range:
number = int(input())

command = ""

if -100 <= number <= 100 and number != 0:
    command = "Yes"
else:
    command = "No"

print(command)
