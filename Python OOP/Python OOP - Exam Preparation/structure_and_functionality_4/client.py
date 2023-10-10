from structure_and_functionality_4.validations import number_starts_with_zero, is_valid_length, contains_only_numbers


class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__validate_phone_number(value)
        self.__phone_number = value

    @staticmethod
    def __validate_phone_number(value):
        number_starts_with_zero(value)
        is_valid_length(value)
        contains_only_numbers(value)
