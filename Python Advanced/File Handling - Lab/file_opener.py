from io import open

try:
    file = open("./text.txt", "r").close()
    print("File found")
except FileNotFoundError:
    print("File not found")
