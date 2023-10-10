from django.shortcuts import render, redirect

from my_music_app.albums.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from my_music_app.albums.models import Album


# Create your views here.


def add_album(request):
    if request.method == "GET":
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'albums/add-album.html', context)


def details_album(request, album_id):
    album = Album.objects.filter(pk=album_id).get()

    context = {
        'album': album,
    }

    return render(request, 'albums/album-details.html', context)


def delete_album(request, album_id):
    album = Album.objects.filter(pk=album_id).get()

    if request.method == "GET":
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album_id': album_id,
    }

    return render(request, 'albums/delete-album.html', context)


def edit_album(request, album_id):
    album = Album.objects.filter(pk=album_id).get()

    if request.method == "GET":
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album_id': album_id,
    }

    return render(request, 'albums/edit-album.html', context)
