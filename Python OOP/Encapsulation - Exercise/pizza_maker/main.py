class Dough:
    def __init__(self, flour_type, baking_technique, weight):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

    @property
    def flour_type(self):
        return self.__flour_type
