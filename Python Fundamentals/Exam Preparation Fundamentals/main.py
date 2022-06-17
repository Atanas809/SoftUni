def result(my_dict):
    for key, value in my_dict.items():
        print(f"{key}\n  HP: {my_dict[key][0]}\n  MP: {my_dict[key][1]}")

        
def output(my_dict):

    command = input().split(" - ")

    while command[0] != "End":

        if command[0] == "CastSpell":
            hero_name = command[1]
            mp_needed = int(command[2])
            spell_name = command[3]

            if my_dict[hero_name][1] >= mp_needed:
                my_dict[hero_name][1] -= mp_needed
                print(f"{hero_name} has successfully cast {spell_name} and now has {my_dict[hero_name][1]} MP!")

            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif command[0] == "TakeDamage":
            hero_name = command[1]
            damage = int(command[2])
            attacker = command[3]

            if my_dict[hero_name][0] - damage > 0:
                my_dict[hero_name][0] -= damage
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {my_dict[hero_name][0]} HP left!")

            else:
                del my_dict[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")

        elif command[0] == "Recharge":
            hero_name = command[1]
            amount = int(command[2])

            if my_dict[hero_name][1] + amount > 200:
                diff = abs(200 - my_dict[hero_name][1])
                my_dict[hero_name][1] = 200
                print(f"{hero_name} recharged for {diff} MP!")

            else:
                my_dict[hero_name][1] += amount
                print(f"{hero_name} recharged for {amount} MP!")

        else:
            hero_name = command[1]
            amount = int(command[2])

            if my_dict[hero_name][0] + amount > 100:
                diff = abs(100 - my_dict[hero_name][0])
                my_dict[hero_name][0] = 100
                print(f"{hero_name} healed for {diff} HP!")

            else:
                my_dict[hero_name][0] += amount
                print(f"{hero_name} healed for {amount} HP!")

        command = input().split(" - ")

    result(my_dict)
