from django.shortcuts import render, redirect

from online_library.books.models import Book
from online_library.core.get_user_profile import get_profile
from online_library.profiles.forms import ProfileCreateForm


# Create your views here.


def index(request):
    profile = get_profile()

    if not profile:
        return add_profile(request)

    books = Book.objects.all()

    context = {
        'books': books,
        'profile': profile,
    }

    return render(request, 'common/home-with-profile.html', context)


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
