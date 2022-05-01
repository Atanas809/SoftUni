from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = float(input("Enter your amount: "))
from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()

print(f"\n{amount} {from_currency} <------> {to_currency}")

converted_currency = c.convert(from_currency, to_currency, amount)

print(f"\n{converted_currency:.2f} {to_currency}")


def auto(w1, w2):

    word1 = w1.lower()
    word2 = w2.lower()

    return f"{sorted(word1)} - {sorted(word2)}"

print(auto("cinema", "iceman"))
print(auto("cool", "loco"))
print(auto("men", "woman"))

