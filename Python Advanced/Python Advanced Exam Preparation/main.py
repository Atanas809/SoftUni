command = input()
command = command.replace("(", "")
command = command.replace(")", "")
command = command.replace(",", " ")
row, col = [int(x) for x in command.split()]