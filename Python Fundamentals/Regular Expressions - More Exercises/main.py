import re

def output(attack_planets, destroyed_planets):
    for key, value in attack_planets.items():
        value = sorted(value)
        print(f"Attacked planets: {len(value)}")
        if len(value) > 0:
            for planet in value:
                print(f"-> {planet}")
