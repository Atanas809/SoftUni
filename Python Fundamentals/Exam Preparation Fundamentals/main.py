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
