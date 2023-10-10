from django.shortcuts import render, redirect

from core.utils import get_profile
from gamesplay_app.games.models import Game
from gamesplay_app.profiles.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from gamesplay_app.profiles.models import Profile
from gamesplay_app.profiles.utils import get_avg_rating


# Create your views here.


def create_profile(request):
    if request.method == "GET":
        form = CreateProfileForm()

    else:
        form = CreateProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profiles/create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    games = Game.objects.all()
    full_name = None
    avg_game_rating = 0.0

    if games:
        avg_game_rating = get_avg_rating(games)

    if profile.first_name and profile.last_name:
        full_name = f"{profile.first_name} {profile.last_name}"

    context = {
        'profile': profile,
        'full_name': full_name,
        'games': games,
        'games_count': games.count(),
        'avg_game_rating': avg_game_rating,
    }

    return render(request, 'profiles/details-profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == "GET":
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
    }

    return render(request, 'profiles/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == "GET":
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profiles/delete-profile.html', context)
