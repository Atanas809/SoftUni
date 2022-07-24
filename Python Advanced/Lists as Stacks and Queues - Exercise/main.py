from collections import deque
from time import strftime
from time import gmtime
import sys


def robots():
    current_robots = deque()

    data = input().split(";")

    for r in data:
        current_robots.append(r)

    return current_robots


def seconds():
    info = list(map(int, input().split(":")))

    current_time = (info[0] * 3600) + (info[1] * 60) + info[2]

    return current_time


def items():
    command = input()
