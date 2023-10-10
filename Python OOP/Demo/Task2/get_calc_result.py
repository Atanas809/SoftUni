from abc import ABC, abstractmethod


class CalcResult(ABC):
    def __init__(self, first_num, second_num, operator):
        self.first_num = first_num
        self.second_num = second_num
        self.operator = operator

    @abstractmethod
    def get_result(self):
        pass
