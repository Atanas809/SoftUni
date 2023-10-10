from django.shortcuts import render, redirect

from prep_exam01.albums.models import Album
from prep_exam01.core.get_user_profile import get_profile


# Create your views here.


def index(request):
    profile = get_profile()

    if not profile:
        return redirect('create profile')

    albums = Album.objects.all()

    context = {
        'albums': albums,
    }

    return render(request, 'common/home-with-profile.html', context)
