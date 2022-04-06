speed = float(input())

if speed <= 10:
    print("too slow")
elif speed <= 50:
    print("average")
elif speed <= 150:
    print("too fast")
elif speed <= 1000:
    print("ultra fast")
else:
    print("extremely fast, please slow down")
