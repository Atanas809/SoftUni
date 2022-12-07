class SteamUser:
    def __init__(self, username, games: []):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        if game not in self.games:
            return f"{game} is not in library"
