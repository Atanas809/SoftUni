text = input()

digits = ""
letters = ""
symbols = ""

for char in text:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        symbols += char

print(f"{digits}\n{letters}\n{symbols}")
