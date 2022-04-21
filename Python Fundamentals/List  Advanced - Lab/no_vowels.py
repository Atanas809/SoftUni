text = input()

vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']

print(f"{''.join([xfor x in text if x not in vowels])}")
