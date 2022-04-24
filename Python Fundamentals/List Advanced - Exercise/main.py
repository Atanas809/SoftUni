# Web-automation:

# import webbrowser as wb

# def web_automation():
#     chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#     URLS = ('softuni.bg', 'stackoverflow.com', 'github.com')

#     for url in URLS:
#         print("Opening..." + url)
#         wb.get(chrome_path).open(url)

# web_automation()

# Forex converter:

from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = int(input('Enter amount: '))
from_currency = input('From currency: ').upper()
to_currency = input('To currency: ').upper()

print(amount, from_currency, "<-----|------>", to_currency)

result = c.convert(from_currency, to_currency, amount)

print(f"{result:.2f}")

