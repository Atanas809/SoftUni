numbers = list(map(int, input().split(", ")))


positive_numbers = [str(x) for x in numbers if x >= 0]
negatives = [str(x) for x in numbers if x < 0]
even = [str(x) for x in numbers if x % 2 == 0]
odd = [str(x) for x in numbers if x % 2 != 0]

print(f"Positive: {', '.join(positive_numbers)}")
print(f"Negative: {', '.join(negatives)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
