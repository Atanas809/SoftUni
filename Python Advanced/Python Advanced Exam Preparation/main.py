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
