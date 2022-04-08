# Задача 1:
import sys

first_number = int(input())
second_number = int(input())
third_number = int(input())

max_number = -sys.maxsize

if first_number > max_number:
    max_number = first_number
if second_number > max_number:
    max_number = second_number
if third_number > max_number:
    max_number = third_number

print(max_number)
