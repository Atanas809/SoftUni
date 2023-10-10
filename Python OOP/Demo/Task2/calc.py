from functools import reduce

from Task2.get_calc_result import CalcResult


class Calculator(CalcResult):
    def __init__(self, first_num, second_num, operator):
        super().__init__(first_num, second_num, operator)

    @property
    def first_num(self):
        return self.__first_num

    @first_num.setter
    def first_num(self, value):
        self.__validate_first_num(value)
        self.__first_num = value

    @property
    def second_num(self):
        return self.__second_num

    @second_num.setter
    def second_num(self, value):
        self.__validate_second_num(value)
        self.__second_num = value

    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, value):
        self.__validate_operator(value)
        self.__operator = value

    @staticmethod
    def __validate_first_num(value):
        if not isinstance(value, int):
            raise Exception('Number must be integer!')

    @staticmethod
    def __validate_second_num(value):
        if not isinstance(value, int):
            raise Exception('Number must be integer!')

    @staticmethod
    def __validate_operator(value):
        valid_operators = ['-', '+', '*', '/']

        if value not in valid_operators:
            raise Exception('Please enter valid operator: (-) (+) (/) (*)')

    @staticmethod
    def final_result(first, second, operator):
        output = float('-inf')

        if operator == '+':
            my_list = [first, second]
            output = reduce(lambda x, y: x + y, my_list)
        elif operator == '-':
            my_list = [first, second]
            output = reduce(lambda x, y: x - y, my_list)
        elif operator == '*':
            my_list = [first, second]
            output = reduce(lambda x, y: x * y, my_list)
        elif operator == '/':
            my_list = [first, second]
            output = int(reduce(lambda x, y: x / y, my_list))

        return output

    def get_result(self):
        result = self.final_result(self.first_num, self.second_num, self.operator)

        if result % 2 == 0:
            return f'Result: {result} (Even)'
        else:
            return f'Result: {result} (Odd)'
