from django.shortcuts import render, redirect

from my_music_app.albums.models import Album
from core.utils import get_profile
from my_music_app.profiles.forms import ProfileCreateForm


# Create your views here.

def index(request):
    profile = get_profile()

    if not profile:
        return add_profile(request)

    albums = Album.objects.all()

    context = {
        'profile': profile,
        'albums': albums,
    }

    return render(request, 'common/home-with-profile.html', context)


def add_profile(request):
    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'common/home-no-profile.html', context)
