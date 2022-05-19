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
 
