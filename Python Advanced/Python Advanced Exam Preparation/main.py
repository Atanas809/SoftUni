from collections import deque

# Test input:
"""
105 20 30 25
120 60 11 400 10 1
"""


def other_operations(material, magic, items, result):
    if result < 100:
        if result % 2 == 0:
            material *= 2
            magic *= 3
            final_result = material + magic
            valid_values(final_result, items)
        else:
            material *= 2
            magic *= 2
            final_result = material + magic
            valid_values(final_result, items)
    elif result > 499:
        material //= 2
        magic //= 2
        final_result = material + magic
        valid_values(final_result, items)


def valid_values(result, items):
    if 100 <= result <= 199:
        items["Gemstone"] += 1
    elif 200 <= result <= 299:
        items["Porcelain Sculpture"] += 1
    elif 300 <= result <= 399:
        items["Gold"] += 1
    elif 400 <= result <= 499:
        items["Diamond Jewellery"] += 1
