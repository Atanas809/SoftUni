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

    current_products = deque()

    while command != "End":
        current_products.append(command)

        command = input()

    return current_products


def output(current_robot, current_product, time_in_seconds):
    hours = strftime("%H:%M:%S", gmtime(time_in_seconds))

    return f"{current_robot} - {current_product} [{hours}]"


current_robots = robots()

processing_time = dict()
fast_robot = ""

fast = sys.maxsize
all_robots = deque()

for r in current_robots:

    robot, time = r.split("-")
    processing_time[robot] = int(time)
    all_robots.append(robot)

    if int(time) < fast:
        fast = int(time)
        fast_robot = robot

time_in_seconds = seconds()
products = items()

working_robots = dict()

while products:
    current_product = products.popleft()
    time_in_seconds += 1

    for robot_name in [k for k in working_robots.keys()]:
        working_robots[robot_name] -= 1
        if working_robots[robot_name] <= 0:
            working_robots.pop(robot_name)
            all_robots.append(robot_name)

    if len(all_robots) > 0:
        current_robot = all_robots.popleft()
        working_robots[current_robot] = processing_time[current_robot]
        print(output(current_robot, current_product, time_in_seconds))
    else:
        products.append(current_product)
