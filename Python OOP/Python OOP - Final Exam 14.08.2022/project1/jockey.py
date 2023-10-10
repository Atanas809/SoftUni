class Jockey:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value

    @staticmethod
    def __validate_name(value):
        if not value or value.isspace():
            raise ValueError("Name should contain at least one character!")

    @staticmethod
    def __validate_age(value):
        if value < 18:
            raise ValueError("Jockeys must be at least 18 to participate in the race!")
