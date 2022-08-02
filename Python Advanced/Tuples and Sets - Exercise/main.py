counter = int(input())

uniques = set()

for _ in range(counter):
    current_elements = set([element for element in input().split()])
    uniques = uniques.union(current_elements)
