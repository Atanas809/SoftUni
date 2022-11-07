# Test input:
"""
6
-----S
----B-
------
------
--B---
--*---
left
down
down
down
left

"""

def is_valid_position(next_row, next_col, size):
    if 0 <= next_row < size and 0 <= next_col < size:
        return True

    return False


def move(row, col, direction):
    if direction == "up":
        return row - 1, col
    elif direction == "down":
        return row + 1, col
    elif direction == "left":
        return row, col - 1
    elif direction == "right":
        return row, col + 1


size = int(input())

burrows = []
field = []
snake_row, snake_col = None, None

for row in range(size):
    current_row_el = [x for x in input()]
    if "S" or "B" in current_row_el:
        for col in range(size):
            if current_row_el[col] == "S":
                snake_row = row
                snake_col = col
            elif current_row_el[col] == "B":
                burrows.append([row, col])
    field.append(current_row_el)

out_of_the_field = False
food_eaten = 0
