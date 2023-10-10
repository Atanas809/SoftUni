from Task1.calc import calculator
from Task1.currency_converter import converter
from Task1.text import enter_text


def open_specific_program(num):
    if num == 1:
        enter_text()
    elif num == 2:
        calculator()
    else:
        converter()
