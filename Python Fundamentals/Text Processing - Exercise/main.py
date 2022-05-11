def is_winning(ticket, symbols):

    l_side = ticket[:10]
    r_side = ticket[10:]

    left = ""
    right = ""


    for s in symbols:

        if s in l_side:
            if s * 6 in l_side:
                left = s * 6

            if s * 7 in l_side:
                left = s * 7

            if s * 8 in l_side:
                left = s * 8

            if s * 9 in l_side:
                left = s * 9

        if s in r_side:
            if s * 6 in r_side:
                right = s * 6

            if s * 7 in r_side:
                right = s * 7

            if s * 8 in r_side:
                right = s * 8

            if s * 9 in r_side:
                right = s * 9

    if left != "" and right != "":

        if left == right:
            print(f'ticket "{ticket}" - {len(left)}{left[0]}')

        else:
            diff = abs(len(left) - len(right))

            if len(left) > len(right):
                print(f'ticket "{ticket}" - {len(right)}{right[0]}')

            elif len(left) < len(right):
                print(f'ticket "{ticket}" - {len(left)}{left[0]}')

    else:
        print(f'ticket "{ticket}" - no match')
        
def is_jackpot(ticket, symbols):

    condition = False

    for x in symbols:
        if x * 20 == ticket:
            condition = True
            break

    if condition:
        return True

def tickets():

    data = input().split(", ")

    symbols = "@#$^"

    for x in data:

        current_ticket = x.strip()

        jackpot = False

        if len(current_ticket) == 20:
            if is_jackpot(current_ticket, symbols):
                jackpot = True
                print(f'ticket "{current_ticket}" - 10{current_ticket[0]} Jackpot!')

            if not jackpot:
                is_winning(current_ticket, symbols)

        else:
            print("invalid ticket")

tickets()

