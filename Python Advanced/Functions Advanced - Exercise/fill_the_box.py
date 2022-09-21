from collections import deque


def fill_the_box(height, length, width, *args):
    box_volume = height * length * width

    cubes = deque(args)

    cubes_left = 0

    while cubes:
        current_cube = cubes.popleft()

        if current_cube == "Finish":
            break

        if box_volume >= current_cube:
            box_volume -= current_cube

        else:
            current_cube -= box_volume
            box_volume = 0
            cubes_left += current_cube

    if cubes_left:
        return f"No more free space! You have {cubes_left} more cubes."
    else:
        return f"There is free space in the box. You could put {box_volume} more cubes."


# Test inputs:
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
