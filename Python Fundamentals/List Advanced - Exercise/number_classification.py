numbers = list(map(int, input().split(", ")))


positives = [str(x) for x in numbers if x >= 0]
negatives = [str(x) for x in numbers if x < 0]
even = [str(x) for x in numbers if x % 2 == 0]
odd = [str(x) for x in numbers if x % 2 != 0]

print(f"Positive: {', '.join(positives)}")
print(f"Negative: {', '.join(negatives)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
