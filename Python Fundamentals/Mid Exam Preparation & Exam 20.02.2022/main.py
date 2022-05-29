animals = input().split(", ")

reverse = list(reversed(animals))

for x in range(len(reverse)):
      if reverse[0] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif reverse[x] == "wolf":
