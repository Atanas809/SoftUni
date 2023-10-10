from abc import ABC, abstractmethod


class ConverterResult(ABC):
    def __init__(self, amount, from_currency, to_currency):
        self.amount = amount
        self.from_currency = from_currency
        self.to_currency = to_currency

    @abstractmethod
    def get_result(self):
        pass