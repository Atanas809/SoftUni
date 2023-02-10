from football_team_generator.player import Player
from football_team_generator.team import Team


p = Player("Pall", 1, 3, 5, 7)

print("Player name:", p.name)
print("Points sprint:", p._Player__sprint)
print("Points dribble:", p._Player__dribble)
print("Points passing:", p._Player__passing)
print("Points shooting:", p._Player__shooting)

print("\ncalling the __str__ method")
print(p)

print("\nAbout the team")
t = Team("Best", 10)
print("Team name:", t._Team__name)
