from collections import deque


def fill_the_box(height, length, width, *args):
    box_volume = height * length * width

    cubes = deque(args)

    cubes_left = 0
