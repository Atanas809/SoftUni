text = input().lower()

counter = 0

if "sand" in text:
    counter += text.count("sand")
if "water" in text:
    counter += text.count("water")
if "fish" in text:
    counter += text.count("fish")
if "sun" in text:
    counter += text.count("sun")
    
print(counter)
