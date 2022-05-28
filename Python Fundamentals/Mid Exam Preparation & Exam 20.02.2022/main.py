text = input().lower()

counter = 0

if "sand" in text:
    counter += text.count("sand")
if "water" in text:
    counter += text.count("water")
