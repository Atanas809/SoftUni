def is_vip(current_guest):
    if current_guest[0].isdigit():
        return True


def output(vip, regular, came):
    for guest in came:
        if is_vip(guest):
            vip.remove(guest)
        else:
            regular.remove(guest)

    print(len(vip) + len(regular))
    if vip:
        [print(name) for name in sorted(vip)]
    if regular:
        [print(name) for name in sorted(regular)]


def party():
    counter = int(input())

    vip_guests = set()
    regular_guests = set()

    for _ in range(counter):
        current_guest = input()

        if is_vip(current_guest):
            vip_guests.add(current_guest)
        else:
            regular_guests.add(current_guest)
