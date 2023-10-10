from django.shortcuts import render, redirect

from core.utils import get_profile
from my_music_app.albums.models import Album
from my_music_app.profiles.forms import ProfileDeleteForm
from my_music_app.profiles.models import Profile


# Create your views here.


def details_profile(request):
    profile = get_profile()
    albums = Album.objects.all().count()

    context = {
        'profile': profile,
        'albums_count': albums,
    }
    return render(request, 'profiles/profile-details.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == "GET":
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profiles/profile-delete.html', context)
