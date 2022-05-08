text = input()

encrypted = ""

for x in text:
    encrypted += chr(ord(x) + 3)

print(encrypted)
