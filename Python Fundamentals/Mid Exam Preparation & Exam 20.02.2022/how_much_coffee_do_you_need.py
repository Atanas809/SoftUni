commands = input()

counter = 0
need_sleep = False

while commands != "END":
    if counter >= 5:
        need_sleep = True
        print("You need extra sleep")
        break
    elif commands == "coding" or commands == "movie":
        counter += 1
    elif commands == "CODING" or commands == "MOVIE":
        counter += 2
    elif commands == "dog" or commands == "cat":
        counter += 1
    elif commands == "DOG" or commands == "CAT":
        counter += 2
        
    commands = input()

if not need_sleep:
    print(counter)
