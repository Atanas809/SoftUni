from collections import deque

bowls_of_ramen = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])

while bowls_of_ramen and customers:
    current_bowl = bowls_of_ramen.pop()
    current_customer = customers.popleft()
