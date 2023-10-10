from Task2.opener import open_specific_program
from Task2.validations import validate_num

enter_num = int(input('Choose a number 1 or 2:'
                      '\n( 1 ) - Text length'
                      '\n( 2 ) - Calculator'
                      '\n( 3 ) - Converter'
                      '\nEnter here -> '))

validate_num(enter_num)
program = open_specific_program(enter_num)

print(program.get_result())
