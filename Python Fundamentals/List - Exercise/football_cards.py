

red_cards = input().split()

a_team = 11
b_team = 11

is_stopped = False

sent_off_players = list()

for x in red_cards:

    if is_stopped:
        break

    else:
        info = x.split("-")

        team = info[0]
        player = info[1]

        if team == "A":
            if a_team < 7:
                is_stopped = True
                break
            else:
                if x not in sent_off_players:
                    sent_off_players.append(x)
                    a_team -= 1

        elif team == "B":
            if b_team < 7:
                is_stopped = True
                break
            else:
                if x not in sent_off_players:
                    sent_off_players.append(x)
                    b_team -= 1


print(f"Team A - {a_team}; Team B - {b_team}")

if is_stopped:
    print("Game was terminated")
