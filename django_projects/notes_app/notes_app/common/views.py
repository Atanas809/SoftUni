from django.shortcuts import render

from core.utils import get_profile
from notes_app.notes.models import Note
from notes_app.profiles.views import add_profile


# Create your views here.


def index(request):
    profile = get_profile()

    if not profile:
        return add_profile(request)

    notes = Note.objects.all()

    context = {
        'notes': notes
    }

    return render(request, 'common/home-with-profile.html', context)
