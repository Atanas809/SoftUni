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
