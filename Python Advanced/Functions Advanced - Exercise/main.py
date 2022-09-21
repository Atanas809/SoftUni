from collections import deque


def fill_the_box(height, length, width, *args):
    box_volume = height * length * width

    cubes = deque(args)

    cubes_left = 0

    while cubes:
        current_cube = cubes.popleft()

        if current_cube == "Finish":
            break
