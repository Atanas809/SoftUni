numbers = list(map(int, input().split(", ")))


positive_numbers = [str(x) for x in numbers if x >= 0]
negative_numbers = [str(x) for x in numbers if x < 0]
even_numbers = [str(x) for x in numbers if x % 2 == 0]
odd_numbers = [str(x) for x in numbers if x % 2 != 0]

print(f"Positive: {', '.join(positive_numbers)}")
print(f"Negative: {', '.join(negative_numbers)}")
print(f"Even: {', '.join(even_numbers)}")
print(f"Odd: {', '.join(odd_numbers)}")
