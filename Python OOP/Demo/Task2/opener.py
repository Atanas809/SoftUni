from Task2.calc import Calculator
from Task2.currency_converter import CurrencyConverter
from Task2.text import Text


def open_specific_program(num):
    if num == 1:
        print('-' * 30)
        return Text(input('Enter your text (must be between 3 and 16 chars): '))
    elif num == 2:
        print('-' * 30)
        first_num = int(input('Enter first number: '))
        second_num = int(input('Enter second number: '))
        operator = input('Enter operator: ')
        return Calculator(first_num, second_num, operator)
    else:
        print('-' * 30)

        amount = float(input('Enter your amount: '))
        from_currency = input('From currency: ').upper()
        to_currency = input('To currency: ').upper()
        return CurrencyConverter(amount, from_currency, to_currency)
