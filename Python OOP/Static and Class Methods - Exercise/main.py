# from math import ceil
#
# x = 21
# y = 4
#
# result = x / y
#
# print(ceil(result))
#
# matrix = [[] for _ in range(2)]
#
# print(matrix)

photos = [["sdsdf", "sdfsdf", "sgg", ""]]
result = ""

for page in photos:
    photo = ["[]" if x else "" for x in page]
    print(photo)
    result += ' '.join(photo)

print(result)

# result = "[] [] []"
# res = result.split(" ")
# print(res)
# print(' '.join(res))