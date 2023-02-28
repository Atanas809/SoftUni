
    def weight(self, value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight = value
