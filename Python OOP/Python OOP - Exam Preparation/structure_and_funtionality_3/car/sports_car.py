from structure_and_funtionality_3.car.car import Car


class SportsCar(Car):
    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

    @property
    def min_speed(self):
        return 400

    @property
    def max_speed(self):
        return 600

    def car_type(self):
        return "SportsCar"
