def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    if not isinstance(length, int) or not isinstance(width, int):
