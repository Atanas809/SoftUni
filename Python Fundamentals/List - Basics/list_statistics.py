number = int(input())

positive_list = list()
negative_list = list()

for _ in range(number):

    num = int(input())

    if num >= 0:
        positive_list.append(num)
    else:
        negative_list.append(num)

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")
