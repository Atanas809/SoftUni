from forex_python.converter import CurrencyRates

from Task1.validations import validate_currency


def converter():
    c = CurrencyRates()

    amount = float(input('Enter your amount: '))
    from_currency = input('From currency: ').upper()
    validate_currency(from_currency)
    to_currency = input('To currency: ').upper()
    validate_currency(to_currency)

    print(amount, from_currency, "<----|---->", to_currency)

    result = c.convert(from_currency, to_currency, amount)

    print(f"{result:.2f} {to_currency}")
