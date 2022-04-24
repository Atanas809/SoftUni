# Forex converter:

from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = int(input('Enter amount: '))
from_currency = input('From currency: ').upper()
to_currency = input('To currency: ').upper()

print(amount, from_currency, "<-----|------>", to_currency)

result = c.convert(from_currency, to_currency, amount)

print(f"{result:.2f}")

