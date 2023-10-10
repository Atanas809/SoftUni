from django.shortcuts import render

from core.utils import get_profile
from gamesplay_app.games.models import Game


# Create your views here.

def index(request):
    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'common/home-page.html', context)


def dashboard(request):
    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, 'common/dashboard.html', context)
