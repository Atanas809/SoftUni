from structure_and_funtionality_3.car.muscle_car import MuscleCar
from structure_and_funtionality_3.car.sports_car import SportsCar
from structure_and_funtionality_3.driver import Driver
from structure_and_funtionality_3.race import Race


class Controller:
    VALID_CAR_TYPES = ["MuscleCar", "SportsCar"]

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):

        if car_type in self.VALID_CAR_TYPES:
            existing_car = self.__find_car_by_model(model)

            if existing_car:
                raise Exception(f"Car {model} is already created!")

            car = self.__create_car_by_type(car_type, model, speed_limit)

            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        existing_driver = self.__find_driver_by_name(driver_name)

        if existing_driver:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)

        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        existing_race = self.__find_race_by_name(race_name)

        if existing_race:
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)

        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        existing_driver = self.__find_driver_by_name(driver_name)

        if not existing_driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        existing_car = self.__find_car_by_type(car_type)

        if not existing_car:
            raise Exception(f"Car {car_type} could not be found!")

        if existing_driver.car is not None:
            old_model = existing_driver.car.model
            existing_driver.car.is_taken = False

            existing_driver.car = existing_car
            existing_car.is_taken = True
            new_model = existing_car.model
            return f"Driver {driver_name} changed his car from {old_model} to {new_model}."

        existing_driver.car = existing_car
        existing_car.is_taken = True
        return f"Driver {driver_name} chose the car {existing_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        existing_race = self.__find_race_by_name(race_name)

        if not existing_race:
            raise Exception(f"Race {race_name} could not be found!")

        existing_driver = self.__find_driver_by_name(driver_name)

        if not existing_driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if existing_driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        already_in_race = self.__find_driver_in_race(existing_race, existing_driver)

        if already_in_race:
            return f"Driver {driver_name} is already added in {race_name} race."

        existing_race.drivers.append(existing_driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        existing_race = self.__find_race_by_name(race_name)

        if not existing_race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(existing_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        first, second, third = self.__sort_drivers_by_speed(existing_race)

        first.number_of_wins += 1
        second.number_of_wins += 1
        third.number_of_wins += 1

        return f"Driver {first.name} wins the {race_name} race with a speed of {first.car.speed_limit}.\n" \
               f"Driver {second.name} wins the {race_name} race with a speed of {second.car.speed_limit}.\n" \
               f"Driver {third.name} wins the {race_name} race with a speed of {third.car.speed_limit}."

    @staticmethod
    def __create_car_by_type(car_type, model, speed_limit):
        if car_type == "MuscleCar":
            return MuscleCar(model, speed_limit)
        else:
            return SportsCar(model, speed_limit)

    @staticmethod
    def __find_driver_in_race(existing_race, existing_driver):
        if existing_driver in existing_race.drivers:
            return True
        return False

    @staticmethod
    def __sort_drivers_by_speed(existing_race):
        sorted_race = sorted(existing_race.drivers, key=lambda x: -x.car.speed_limit)

        return [sorted_race[0], sorted_race[1], sorted_race[2]]

    def __find_car_by_model(self, model):
        for car in self.cars:
            if car.model == model:
                return car

    def __find_driver_by_name(self, driver_name) -> Driver:
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

    def __find_race_by_name(self, race_name) -> Race:
        for race in self.races:
            if race.name == race_name:
                return race

    def __find_car_by_type(self, car_type):
        for i in range(len(self.cars) - 1, -1, -1):
            car = self.cars[i]
            if car.car_type() == car_type and not car.is_taken:
                return car
