from os import remove
from os.path import exists

# Slower operation:
try:
    file = "./my_first_file.txt"
    remove(file)
except FileNotFoundError:
