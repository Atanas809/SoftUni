commands = input()

counter = 0
need_sleep = False

while commands != "END":
    if counter >= 5:
        need_sleep = True
        print("You need extra sleep")
        break
    elif commands == "coding" or commands == "movie":
