from os import remove
from os.path import exists

# Slower operation:
try:
    file = "./my_first_file.txt"
    remove(file)
except FileNotFoundError:
    print("File already deleted!")


# Faster operation:
file = "./my_first_file.txt"

if exists(file):
    remove(file)
else:
    print("File already deleted!")
    
