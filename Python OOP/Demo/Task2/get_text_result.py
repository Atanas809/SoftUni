from abc import ABC, abstractmethod


class OutputText(ABC):
    def __init__(self, data):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__validate_data(value)
        self.__data = value

    @staticmethod
    def __validate_data(value):
        if len(value) < 3 or len(value) > 16:
            raise Exception('Text must be between 3 and 16 chars')

    @abstractmethod
    def get_result(self):
        pass
