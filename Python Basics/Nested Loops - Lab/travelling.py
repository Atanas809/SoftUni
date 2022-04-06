command = input()

while command != "End":
    destination = command
    budget = float(input())
    total_saved_money = 0
    enough_money_for_trip = False
    while total_saved_money < budget:
        saved_money = float(input())
        total_saved_money += saved_money
        if total_saved_money >= budget:
            enough_money_for_trip = True
            break
    if enough_money_for_trip:
        print(f"Going to {destination}!")
    command = input()

