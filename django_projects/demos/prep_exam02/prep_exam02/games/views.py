from django.shortcuts import render, redirect

from prep_exam02.games.forms import GameCreateForm, GameEditForm, GameDeleteForm
from prep_exam02.games.models import Game


# Create your views here.

def add_game(request):
    if request.method == 'GET':
        create_form = GameCreateForm()

    else:
        create_form = GameCreateForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect('dashboard')

    context = {
        'create_form': create_form,
    }

    return render(request, 'games/create-game.html', context)


def details_game(request, id):
    game = Game.objects.filter(pk=id).get()

    context = {
        'game': game,
    }

    return render(request, 'games/details-game.html', context)


def delete_game(request, id):
    game = Game.objects.filter(pk=id).get()

    if request.method == 'GET':
        delete_form = GameDeleteForm(instance=game)

    else:
        delete_form = GameDeleteForm(request.POST, instance=game)

        if delete_form.is_valid():
            delete_form.save()
            return redirect('dashboard')

    context = {
        'delete_form': delete_form,
        'game_id': id,
    }

    return render(request, 'games/delete-game.html', context)


def edit_game(request, id):
    game = Game.objects.filter(pk=id).get()

    if request.method == 'GET':
        edit_form = GameEditForm(instance=game)

    else:
        edit_form = GameEditForm(request.POST, instance=game)

        if edit_form.is_valid():
            edit_form.save()
            return redirect('dashboard')

    context = {
        'edit_form': edit_form,
        'game_id': id,
    }

    return render(request, 'games/edit-game.html', context)
