from web_final_exam_2022.cars.models import Car
from web_final_exam_2022.profiles.models import Profile


def get_user_profile():
    profile = Profile.objects.all()

    if profile:
        return profile.get()
    return None


def get_total_cars_prices():
    cars = Car.objects.all()
    total_sum = 0

    if cars:
        total_sum = sum(car.price for car in cars)

    return total_sum
