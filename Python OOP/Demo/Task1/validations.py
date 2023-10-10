def validate_text(text):
    if len(text) < 3 or len(text) > 16:
        raise Exception('Text must be between 3 and 16 chars')


def validate_num(num):
    valid_nums = [1, 2, 3]
    if num in valid_nums:
        pass
    else:
        raise Exception('Enter valid number 1 or 2')


def validate_operator(operator):
    valid_operators = '-+/*'

    if operator not in valid_operators:
        raise Exception('Please enter valid operator: (-) (+) (/) (*) ')


def validate_currency(currency):
    valid_currencies = ['BGN', 'EUR', 'USD', 'CNY', 'RUB']

    if currency not in valid_currencies:
        raise Exception('Enter valid currency: (BGN), (EUR), (USD), (CNY), (RUB)')
