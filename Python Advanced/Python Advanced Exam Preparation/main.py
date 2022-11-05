# Test input:
"""
3, 1, 10, 1, 2
0
"""
jobs = [int(x) for x in input().split(", ")]

needed_index = int(input())
cycles = 0

while True:
    current_index = jobs.index(min(jobs))
    current_value = jobs[current_index]
    if current_index == needed_index:
        cycles += current_value
        break

    cycles += current_value
    jobs[current_index] += max(jobs) + 1
