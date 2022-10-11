# Relative: (based on the location of the current file)
"""
./  ---> current directory
file = open("./text.txt")
print(file.read())

../ ---> previous directory
file = open("../Error Handling - Lab/so_many_exceptions.py")
print(file.read())

"""

# Absolute: (based on OS file location)
"""

file = open("D:\PyCharm Community Edition 2021.2.2\Advanced Python\Error Handling - Lab/repeat_text.py")
print(file.read())

"""

# Relative path transformed to Absolute path:
"""

print(os.path.abspath("../Error Handling - Lab/repeat_text.py"))

"""

# Path separator:
"""
