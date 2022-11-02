def element_on_position(next_row, next_col, field):
    if field[next_row][next_col] == "R":
        return "R"
    elif field[next_row][next_col] == "W":
        return "W"
    elif field[next_row][next_col] == "M":
        return "M"
    elif field[next_row][next_col] == "C":
        return "C"


def opposite_side(next_row, next_col, size, field):
    if next_row < 0:
        return size - 1, next_col
    elif next_row == size:
        return 0, next_col
    elif next_col < 0:
        return next_row, size - 1
    elif next_col == size:
        return next_row, 0


def is_outside(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return False

    return True


def move(row, col, command):
    if command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col
    elif command == "left":
        return row, col - 1
    elif command == "right":
        return row, col + 1


size = 6
rover_row, rover_col = None, None
field = []

for row in range(size):
    current_row_el = [x for x in input().split(" ")]
    if "E" in current_row_el:
        rover_row = row
        rover_col = current_row_el.index("E")
    field.append(current_row_el)

commands = input().split(", ")

field[rover_row][rover_col] = "-"

deposits = {
    "M": 0,
    "W": 0,
    "C": 0
}


for command in commands:
    next_row, next_col = move(rover_row, rover_col, command)

    if is_outside(next_row, next_col, size):
        next_row, next_col = opposite_side(next_row, next_col, size, field)
        element = element_on_position(next_row, next_col, field)
        if element == "R":
            print(f"Rover got broken at {next_row, next_col}")
            break
        elif element == "W":
            deposits[element] += 1
            print(f"Water deposit found at {next_row, next_col}")
        elif element == "M":
            deposits[element] += 1
            print(f"Metal deposit found at {next_row, next_col}")
        elif element == "C":
            deposits[element] += 1
            print(f"Concrete deposit found at {next_row, next_col}")
