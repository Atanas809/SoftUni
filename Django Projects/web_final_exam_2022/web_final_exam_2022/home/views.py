from django.shortcuts import render

from web_final_exam_2022.cars.models import Car
from web_final_exam_2022.core.utils import get_user_profile


def home_page(request):
    user_profile = get_user_profile()

    context = {
        'user_profile': user_profile,
    }

    return render(request, 'home/index.html', context)


def catalogue_page(request):
    cars = Car.objects.all()
    count_cars = None

    if cars:
        count_cars = cars.count()

    context = {
        'cars': cars,
        'count_cars': count_cars,
    }

    return render(request, 'home/catalogue.html', context)
