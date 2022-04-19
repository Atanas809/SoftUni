def bar(number):
    
    percents = (number // 10) * "%"
    dots = (10 - len(percents)) * "."

    return f"[{percents}{dots}]"

def loading():

    number = int(input())

    if number == 100:
        print(f"100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f"{number}% {bar(number)}")
        print("Still loading...")

loading()
