from collections import deque


def math_operations(*args, **kwargs):

    values = deque(args)
    index = 1

    while values:
        if index > 4:
            index = 1
            continue

        current_value = values.popleft()

        """
        •	The first element should be added to the value of the key "a"
        •	The second element should be subtracted from the value of the key "s"
        •	The third element should be divisor to the value of the key "d"
        •	The fourth element should be multiplied by the value of the key "m"
        """

        if index == 1:
            kwargs["a"] += current_value
        elif index == 2:
            kwargs["s"] -= current_value
        elif index == 3:
            if current_value > 0:
                kwargs["d"] /= current_value
        elif index == 4:
            kwargs["m"] *= current_value

        index += 1

    sorted_dict = dict(sorted(kwargs.items(), key=lambda x: (-x[1], x[0])))

    result = [f"{key}: {value:.1f}" for key, value in sorted_dict.items()]

    return '\n'.join(result)
