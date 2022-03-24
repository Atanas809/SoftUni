hour = int(input())
day = input()

if 10 <= hour <= 18 and day != "Sunday":
    print("open")
else:
    print("closed")
