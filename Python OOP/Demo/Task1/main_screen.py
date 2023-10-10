from Task1.opener import open_specific_program
from validations import validate_num

enter_num = int(input('Choose a number 1 or 2:'
                      '\n( 1 ) - Text length'
                      '\n( 2 ) - Calculator'
                      '\n( 3 ) - Converter'
                      '\nEnter here -> '))

validate_num(enter_num)
open_specific_program(enter_num)
