def extraction():

    file_data = input().split("\\")

    file_name = file_data[-1].split(".")

    print(f"File name: {file_name[0]}\nFile extension: {file_name[1]}")

extraction()
