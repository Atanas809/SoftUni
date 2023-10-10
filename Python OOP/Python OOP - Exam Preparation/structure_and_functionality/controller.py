class Controller:
    VALID_SUPPLY_TYPES = ["Food", "Drink"]

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        currently_added_players = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                currently_added_players.append(player)

        return f"Successfully added: {', '.join([player.name for player in currently_added_players])}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player_by_name(player_name)

        if sustenance_type not in self.VALID_SUPPLY_TYPES:
            return

        if not player:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        existing_supply, index = self.__get_supply_by_type(sustenance_type)

        if not existing_supply:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        player.stamina = min(player.stamina + existing_supply.energy, 100)
        self.supplies.pop(index)

        return f"{player_name} sustained successfully with {existing_supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        if first_player.stamina == 0 and second_player.stamina == 0:
            result = f"Player {first_player_name} does not have enough stamina.\n"
            result += f"Player {second_player_name} does not have enough stamina."

            return result

        if first_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        elif second_player.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        first_turn = first_player if first_player.stamina < second_player.stamina else second_player
        second_turn = second_player if first_turn == first_player else first_player

        first_player_damage = first_turn.stamina / 2
        second_turn.stamina = max(second_turn.stamina - first_player_damage, 0)

        second_player_damage = second_turn.stamina / 2
        first_turn.stamina = max(first_turn.stamina - second_player_damage, 0)

        if first_turn.stamina == 0:
            return f"Winner: {second_turn.name}"
        elif second_turn.stamina == 0:
            return f"Winner: {first_turn.name}"
        else:
            winner = first_turn if first_turn.stamina > second_turn.stamina else second_turn
            return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            gets_reduced = player.age * 2
            player.stamina = max(player.stamina - gets_reduced, 0)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ""

        for player in self.players:
            result += str(player) + '\n'

        for supply in self.supplies:
            result += supply.details() + '\n'

        return result.strip()

    def __find_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def __get_supply_by_type(self, sustenance_type):
        for idx in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[idx].__class__.__name__ == sustenance_type:
                return self.supplies[idx], idx
        return None, -1
