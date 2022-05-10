def output(unique_symbols, text):

    result = ""

    for t in text:
        number = ""
        chars = ""

        for x in t:
            if x.isdigit():
                number += x
            else:
                chars += x.upper()

        result += chars * int(number)

    print(f"Unique symbols used: {len(unique_symbols)}")
    print(result)
    
def rage():

    data = input()

    unique_symbols = set()

    text = list()

    index = 0

    condition = True

    while index <= len(data) - 1:

        if data[index].isdigit():
            while data[index].isdigit():
                if index < len(data) - 1:
                    index += 1
                else:
                    text.append(data[:index + 1])
                    condition = False
                    break

            if condition:
                text.append(data[:index])
                data = data.replace(data[:index], "", 1)
                index = 0
                continue
        else:
            unique_symbols.add(data[index].lower())

        index += 1

    output(unique_symbols, text)

rage()
