from django.shortcuts import render, redirect

from gamesplay_app.games.forms import CreateGameForm, EditGameForm, DeleteGameForm
from gamesplay_app.games.models import Game


# Create your views here.


def create_game(request):
    if request.method == "GET":
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'games/create-game.html', context)


def details_game(request, game_id):
    game = Game.objects.filter(pk=game_id).get()

    context = {
        'game': game
    }

    return render(request, 'games/details-game.html', context)


def edit_game(request, game_id):
    game = Game.objects.filter(pk=game_id).get()

    if request.method == "GET":
        form = EditGameForm(instance=game)
    else:
        form = EditGameForm(request.POST, instance=game)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game_id': game_id,
    }

    return render(request, 'games/edit-game.html', context)


def delete_game(request, game_id):
    game = Game.objects.filter(pk=game_id).get()

    if request.method == "GET":
        form = DeleteGameForm(instance=game)
    else:
        form = DeleteGameForm(request.POST, instance=game)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game_id': game_id,
    }

    return render(request, 'games/delete-game.html', context)
