from django.shortcuts import render

from prep_exam02.core.utils import get_user_profile
from prep_exam02.games.models import Game


# Create your views here.


def home_page(request):
    profile = get_user_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'home/home-page.html', context)


def dashboard(request):
    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, 'home/dashboard.html', context)
