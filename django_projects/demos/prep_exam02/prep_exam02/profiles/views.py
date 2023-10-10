from django.shortcuts import render, redirect

from prep_exam02.core.utils import get_user_profile, get_avg_rating
from prep_exam02.games.models import Game
from prep_exam02.profiles.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm


# Create your views here.


def add_profile(request):
    if request.method == 'GET':
        create_form = ProfileCreateForm()
    else:
        create_form = ProfileCreateForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect('home page')

    context = {
        'create_form': create_form,
    }

    return render(request, 'profiles/create-profile.html', context)


def details_profile(request):
    profile = get_user_profile()
    games = Game.objects.all()
    games_count = games.count()
    avg_games_rating = None

    if games:
        avg_games_rating = get_avg_rating()

    context = {
        'profile': profile,
        'games': games,
        'games_count': games_count,
        'avg_games_rating': avg_games_rating,
    }

    return render(request, 'profiles/details-profile.html', context)


def delete_profile(request):
    profile = get_user_profile()

    if request.method == 'GET':
        delete_form = ProfileDeleteForm(instance=profile)
    else:
        delete_form = ProfileDeleteForm(request.POST, instance=profile)

        if delete_form.is_valid():
            delete_form.save()
            return redirect('home page')

    context = {
        'delete_form': delete_form,
    }

    return render(request, 'profiles/delete-profile.html', context)


def edit_profile(request):
    profile = get_user_profile()

    if request.method == 'GET':
        edit_form = ProfileEditForm(instance=profile)
    else:
        edit_form = ProfileEditForm(request.POST, instance=profile)

        if edit_form.is_valid():
            edit_form.save()
            return redirect('details profile')

    context = {
        'edit_form': edit_form,
    }

    return render(request, 'profiles/edit-profile.html', context)
