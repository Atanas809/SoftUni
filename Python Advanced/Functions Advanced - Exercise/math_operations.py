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


# Test inputs:
print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
