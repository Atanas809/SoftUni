def explosion():

    text = input()

    index = 0
    power_left = 0

    while index <= len(text) - 1:

        if text[index].isdigit():

            if text[index].isdigit() and text[index] == "1":
                text = text.replace(text[index], "", 1)

            else:
                number = int(text[index])

                if text[index + 1] == ">":
                    power_left += number - 1
                    text = text.replace(text[index], "", 1)

                else:
                    current_string = text[index: index + number + power_left]

                    if ">" not in current_string:
                        l_side = text[:index]
                        r_side = text[index + number + power_left:]
                        text = l_side + r_side
                        power_left = 0
                    else:
                        current_index = 0
                        total_power = number + power_left
                        power_left = 0

                        while current_index <= len(current_string) - 1:
                            if current_string[current_index] != ">":
                                current_string = current_string.replace(current_string[current_index], "", 1)
                                total_power -= 1
                                current_index -= 1
                            else:
                                power_left += total_power
                                break

                            current_index += 1

                        text = text[:index] + current_string + text[index + number:]

        index += 1

    print(text)

explosion()
