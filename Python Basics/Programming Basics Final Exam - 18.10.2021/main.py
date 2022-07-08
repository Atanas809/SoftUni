team = input()
souvenirs = input()
number_of_souvenirs = int(input())
price = 0

team_is_valid = False
souvenirs_is_valid = True

if team == "Argentina":
    team_is_valid = True
    if souvenirs == "flags":
        price += number_of_souvenirs * 3.25
    elif souvenirs == "caps":
        price += number_of_souvenirs * 7.20
    elif souvenirs == "posters":
        price += number_of_souvenirs * 5.10
