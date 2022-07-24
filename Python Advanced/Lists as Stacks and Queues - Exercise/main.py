from collections import deque
from time import strftime
from time import gmtime
import sys


def robots():
    current_robots = deque()

    data = input().split(";")

    for r in data:
        current_robots.append(r)
