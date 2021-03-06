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
    reload += 1

    if reload == size_barrel and bullets:
        reload = 0
        print("Reloading!")
        continue

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    money_earned = intelligence - (bullet_price * bullets_used)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
