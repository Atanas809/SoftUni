from forex_python.converter import CurrencyRates

from Task2.get_converter_result import ConverterResult


class CurrencyConverter(ConverterResult):
    VALID_CURRENCIES = ['BGN', 'EUR', 'USD', 'CNY', 'RUB']

    def __init__(self, amount, from_currency, to_currency):
        super().__init__(amount, from_currency, to_currency)

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__validate_amount(value)
        self.__amount = value

    @property
    def from_currency(self):
        return self.__from_currency

    @from_currency.setter
    def from_currency(self, value):
        self.__validate_currency(value)
        self.__from_currency = value

    @property
    def to_currency(self):
        return self.__to_currency

    @to_currency.setter
    def to_currency(self, value):
        self.__validate_currency(value)
        self.__to_currency = value

    @staticmethod
    def __validate_amount(value):
        if value < 1:
            raise Exception('Amount must be greater than 0!')

    def __validate_currency(self, value):
        if value.upper() not in self.VALID_CURRENCIES:
            raise Exception('Enter valid currency: (BGN), (EUR), (USD), (CNY), (RUB)')

    def get_result(self):
        result = ''

        c = CurrencyRates()

        result += f'{int(self.amount)} {self.from_currency} <----|----> {self.to_currency}\n'

        output = c.convert(self.from_currency, self.to_currency, self.amount)

        result += f"{output:.2f} {self.to_currency}"

        return result
