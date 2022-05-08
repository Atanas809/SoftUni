def output(name1, name2):
    result = 0

    if len(name1) > len(name2):
        index = 0
        while len(name2) - 1 >= index:
            result += ord(name1[index]) * ord(name2[index])

            index += 1

        for x in range(index, len(name1)):
            result += ord(name1[x])
    else:
        for i in range(0, len(name1)):
            result += ord(name1[i]) * ord(name2[i])

    return result

