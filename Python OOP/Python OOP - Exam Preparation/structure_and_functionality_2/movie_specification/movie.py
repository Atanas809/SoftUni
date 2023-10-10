from abc import ABC, abstractmethod

from structure_and_functionality_2.user import User


class Movie(ABC):
    MIN_AGE_RESTRICTION = None

    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__validate_title(value)
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__validate_year(value)
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__validate_owner(value)
        self.__owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        self.__validate_age_restriction(value)
        self.__age_restriction = value
        self.__validate_user_can_watch(self.owner.age)

    def __validate_age_restriction(self, value):
        if value < self.MIN_AGE_RESTRICTION:
            raise ValueError(f"{self.movie_type()} movies must be restricted "
                             f"for audience under {self.MIN_AGE_RESTRICTION} years!")

    @staticmethod
    def __validate_title(value):
        if not value:
            raise ValueError("The title cannot be empty string!")

    @staticmethod
    def __validate_year(value):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")

    @staticmethod
    def __validate_owner(value):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")

    @abstractmethod
    def movie_type(self):
        pass

    @abstractmethod
    def details(self):
        pass

    def __validate_user_can_watch(self, age):
        if age < self.age_restriction:
            raise Exception(f"User must be over {self.age_restriction} to watch this movie")
