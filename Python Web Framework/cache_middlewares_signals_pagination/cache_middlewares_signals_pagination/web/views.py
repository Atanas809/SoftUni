import random
from time import sleep

from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from cache_middlewares_signals_pagination.web.models import Employee

CLICK_COUNT_SESSION_KEY = 'CLICK_COUNT_SESSION_KEY'
LATEST_VALUES_SESSION_KEY = 'LATEST_VALUES_SESSION_KEY'
UserModel = get_user_model()


def very_slow_operation():
    sleep(3)
    return random.randint(1, 1024)


# @cache_page(1 * 60)
def index(request):
    # Employee.objects.create(
    #     first_name = 'Gogo',
    #     last_name='Ivanov',
    #     age=22,
    # )

    value = very_slow_operation()
    latest_values = request.session.get(LATEST_VALUES_SESSION_KEY, [])
    latest_values = [value] + latest_values
    latest_values = latest_values[:3]
    request.session[LATEST_VALUES_SESSION_KEY] = latest_values

    return HttpResponse(f"Value is: {value}; Latest: [{', '.join(str(x) for x in latest_values)}]")


def show_session(request):
    clicks_count = request.session.get(CLICK_COUNT_SESSION_KEY, 0) + 1
    request.session[CLICK_COUNT_SESSION_KEY] = clicks_count

    return HttpResponse(f"Clicks: {clicks_count}")


def raise_error(request):
    UserModel.objects.get(pk=100291)

    return HttpResponse('Hello!!!')