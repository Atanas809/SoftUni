from pyfiglet import figlet_format

# Test input:
"""
Hello World!
"""

text = input()

f = figlet_format(text, font="digital")
print(f)
