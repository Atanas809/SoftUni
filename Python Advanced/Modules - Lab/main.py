from packages.while_stop import while_loop
from packages.create_locate import *

# Test input:
"""
Create Sequence 10
Locate 13
Create Sequence 3
Locate 10
Stop
"""


def fibonacci_sequence():

    result = while_loop("Stop")

    for data in result:
        command = data[0]
        value = int(data[-1])

        if command == "Create":
            create(value)
