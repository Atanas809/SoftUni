from collections import deque

bullet_price = int(input())
size_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence = int(input())

reload = 0
bullets_used = 0

while bullets and locks:

    current_bullet = bullets.pop()
    current_lock = locks[0]

    if current_lock >= current_bullet:
        locks.remove(current_lock)
        print("Bang!")
    else:
        print("Ping!")

    bullets_used += 1
