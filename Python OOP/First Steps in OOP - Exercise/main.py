class SteamUser:
    def __init__(self, username, games: []):
        self.username = username
        self.games = games
        self.played_hours = 0
