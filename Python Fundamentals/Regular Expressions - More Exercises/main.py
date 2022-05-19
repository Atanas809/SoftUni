import re

def output(attack_planets, destroyed_planets):
    
    for key, value in attack_planets.items():
        value = sorted(value)
        print(f"Attacked planets: {len(value)}")
        if len(value) > 0:
            for planet in value:
                print(f"-> {planet}")
                
    for x, y in destroyed_planets.items():
        y = sorted(y)
        print(f"Destroyed planets: {len(y)}")
         if len(y) > 0:
            for planet in y:
                print(f"-> {planet}")
                
def decrypted(message, attacked, destroyed):

    expression = r"@(?P<planet>([A-Za-z]+))(([^@!\-:>]?)+)" \
                 r":(?P<population>[0-9]+)(([^@!\-:>]?)+)" \
                 r"!(?P<attack_type>[A|D])!(([^@!\-:>]?)+)" \
                 r"->(?P<soldier_count>[0-9]+)"

    matches = re.finditer(expression, message)

    for match in matches:
        planet_name = match.group("planet")
        population = match.group("population")
        attack_type = match.group("attack_type")
        soldiers = match.group("soldier_count")

        if attack_type == "A":
            attacked["Attacked planets:"].append(planet_name)
        elif attack_type == "D":
            destroyed["Destroyed planets:"].append(planet_name)
            
def substraction(data, counter):

    new_message = ""


