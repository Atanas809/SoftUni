from project1.horse_specification.horse import Horse


class Appaloosa(Horse):
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def max_speed(self):
        return 120

    def train(self):
        self.speed = min(self.speed + 2, self.max_speed())
