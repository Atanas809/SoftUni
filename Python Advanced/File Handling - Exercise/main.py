def output(current_line):
    symbols_to_replace = {"-", ",", ".", "!", "?"}

    for symbol in symbols_to_replace:
        if symbol in current_line:
            current_line = current_line.replace(symbol, "@")
