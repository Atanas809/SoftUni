# Задача 1:
text = input()

vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']

print(f"{''.join([i for i in text if i not in vowels])}")