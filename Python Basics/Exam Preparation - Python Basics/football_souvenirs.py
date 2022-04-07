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
    elif souvenirs == "stickers":
        price += number_of_souvenirs * 1.25
    else:
        souvenirs_is_valid = False
if team == "Brazil":
    team_is_valid = True
    if souvenirs == "flags":
        price += number_of_souvenirs * 4.20
    elif souvenirs == "caps":
        price += number_of_souvenirs * 8.50
    elif souvenirs == "posters":
        price += number_of_souvenirs * 5.35
    elif souvenirs == "stickers":
        price += number_of_souvenirs * 1.20
    else:
        souvenirs_is_valid = False
# if team == "Croatia":
#     team_is_valid = True
#     if souvenirs == "flags":
#         price += number_of_souvenirs * 2.75
#     elif souvenirs == "caps":
#         price += number_of_souvenirs * 6.90
#     elif souvenirs == "posters":
#         price += number_of_souvenirs * 4.95
#     elif souvenirs == "stickers":
#         price += number_of_souvenirs * 1.10
#     else:
#         souvenirs_is_valid = False
if team == "Denmark":
    team_is_valid = True
    if souvenirs == "flags":
        price += number_of_souvenirs * 3.10
    elif souvenirs == "caps":
        price += number_of_souvenirs * 6.50
    elif souvenirs == "posters":
        price += number_of_souvenirs * 4.80
    elif souvenirs == "stickers":
        price += number_of_souvenirs * 0.90
    else:
        souvenirs_is_valid = False

if team_is_valid and souvenirs_is_valid:
    print(f"Pepi bought {number_of_souvenirs} {souvenirs} of {team} for {price:.2f} lv.")
elif team_is_valid == False:
    print("Invalid country!")
elif souvenirs_is_valid == False:
    print("Invalid stock!")
