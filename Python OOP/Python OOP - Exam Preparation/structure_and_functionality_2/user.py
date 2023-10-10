import os


class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__validate_username(value)
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value

    @staticmethod
    def __validate_username(value):
        if not value:
            raise ValueError("Invalid username!")

    @staticmethod
    def __validate_age(value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")

    def __str__(self):
        # TODO
        result = f"Username: {self.username}, Age: {self.age}\n"
        result += "Liked movies:\n"
        if self.movies_liked:
            result += os.linesep.join([movie.details() for movie in self.movies_liked]) + '\n'
        else:
            result += "No movies liked.\n"

        result += "Owned movies:\n"
        if self.movies_owned:
            result += os.linesep.join([movie.details() for movie in self.movies_owned])
        else:
            result += "No movies owned.\n"

        return result
