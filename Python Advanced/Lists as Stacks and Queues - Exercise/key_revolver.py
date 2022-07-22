from collections import deque

bullet_price = int(input())
size_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence = int(input())

reload = 0
bullets_used = 0

while bullets and locks:
