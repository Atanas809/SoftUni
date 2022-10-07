from io import open

try:
    file = open("./text.txt", "r").close()
    print("File found")
