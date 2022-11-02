def element_on_position(next_row, next_col, field):
    if field[next_row][next_col] == "R":
        return "R"
    elif field[next_row][next_col] == "W":
        return "W"
    elif field[next_row][next_col] == "M":
        return "M"
    elif field[next_row][next_col] == "C":
        return "C"
