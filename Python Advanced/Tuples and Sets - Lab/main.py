def is_vip(current_guest):
    if current_guest[0].isdigit():
        return True


def output(vip, regular, came):
    for guest in came:
        if is_vip(guest):
            vip.remove(guest)
