from project1.horse_race import HorseRace
from project1.horse_specification.appaloosa import Appaloosa
from project1.horse_specification.thoroughbred import Thoroughbred
from project1.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = ["Appaloosa", "Thoroughbred"]
    UNIQUE_HORSE_RACES_NAMES = []
    VALID_RACE_TYPES = ["Winter", "Spring", "Autumn", "Summer"]

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.VALID_HORSE_TYPES:
            return

        existing_horse = self.__find_horse_by_name(horse_name)

        if existing_horse:
            raise Exception(f"Horse {horse_name} has been already added!")

        get_horse_obj_by_type = self.__horse_type(horse_type)

        horse = get_horse_obj_by_type(horse_name, horse_speed)

        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        existing_jockey = self.__find_jockey_by_name(jockey_name)

        if existing_jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        # TODO: COULD BE HorseRaceApp.UNIQUE_HORSE_RACES_NAMES
        if race_type in self.UNIQUE_HORSE_RACES_NAMES:
            raise Exception(f"Race {race_type} has been already created!")

        horse_race = HorseRace(race_type)
        self.horse_races.append(horse_race)
        self.UNIQUE_HORSE_RACES_NAMES.append(race_type)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_jockey_by_name(jockey_name)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        existing_horse = self.__find_horse_by_type(horse_type)

        if not existing_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = existing_horse
        existing_horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {existing_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__find_race_by_type(race_type)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.__find_jockey_by_name(jockey_name)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__find_race_by_type(race_type)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        max_speed = max([jockey.horse.speed for jockey in race.jockeys])
        winner = self.__find_jockey_with_given_speed(max_speed, race)

        return f"The winner of the {race_type} race, " \
               f"with a speed of {max_speed}km/h " \
               f"is {winner.name}! " \
               f"Winner's horse: {winner.horse.name}."

    def __find_horse_by_name(self, horse_name):
        for horse in self.horses:
            if horse.name == horse_name:
                return horse

    def __find_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey

    def __find_horse_by_type(self, horse_type):
        for index in range(len(self.horses) - 1, -1, -1):
            horse = self.horses[index]
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                return horse

    def __find_race_by_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race

    @staticmethod
    def __find_jockey_with_given_speed(max_speed, race):
        for jockey in race.jockeys:
            if jockey.horse.speed == max_speed:
                return jockey

    @staticmethod
    def __horse_type(horse_type):
        if horse_type == "Appaloosa":
            return Appaloosa
        return Thoroughbred
