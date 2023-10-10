from django.shortcuts import render, redirect

from core.utils import get_profile
from notes_app.notes.models import Note
from notes_app.profiles.forms import ProfileCreateForm


# Create your views here.


def details_profile(request):
    profile = get_profile()
    notes = Note.objects.all()
    notes_count = notes.count()

    http_referer = request.META.get('HTTP_REFERER')

    if '/profile' in http_referer:
        profile.delete()
        notes.delete()
        return redirect('index')

    context = {
        'profile': profile,
        'notes_count': notes_count,
    }

    return render(request, 'profiles/profile.html', context)


def add_profile(request):

    if request.method == 'GET':
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
