class Player:
    UNIQUE_NAMES = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def need_sustenance(self):
        return self.stamina < 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__validate_name_is_unique(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        self.__validate_stamina(value)
        self.__stamina = value

    @staticmethod
    def __validate_name(value):
        if not value:
            raise ValueError("Name not valid!")

    @staticmethod
    def __validate_name_is_unique(value):
        if value in Player.UNIQUE_NAMES:
            raise Exception(f"Name {value} is already used!")
        Player.UNIQUE_NAMES.append(value)

    @staticmethod
    def __validate_age(value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")

    @staticmethod
    def __validate_stamina(value):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
