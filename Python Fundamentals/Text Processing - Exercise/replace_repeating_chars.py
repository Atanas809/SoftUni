text = input()

output = ""

index = 0

for x in text:
    if len(output) == 0:
        output += x
        index += 1
    else:
        if output[index - 1] != x:
            output += x
            index += 1

print(output)
