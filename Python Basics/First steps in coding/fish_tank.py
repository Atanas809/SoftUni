length = int(input())
width = int(input())
height = int(input())
percent = float(input())

area = length * width * height
volume_in_litres = area * 0.001
needed_litres = volume_in_litres * (1 - 0.17)

print(needed_litres)
