number = float(input())

if number == 0:
    print("Your number is zero")
elif number > 0:
    if 0 < number < 1:
        print("small positive")
    elif number > 1000000:
        print("large positive")
    else:
        print("positive")
else:
    if 0 > number > -1:
        print("small negative")
    elif number < -1000000:
        print("large negative")
    else:
        print("negative")
