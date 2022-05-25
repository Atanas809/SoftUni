key = int(input())

number = int(input())

my_list = list()

for x in range(1, number + 1):
    letter = input()
    result = ord(letter) + key
    my_list.append(chr(result))
