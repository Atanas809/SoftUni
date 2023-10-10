from django.shortcuts import render, redirect

from online_library.books.forms import BookCreateForm, BookEditForm
from online_library.books.models import Book
from online_library.core.get_user_profile import get_profile


# Create your views here.

def add_book(request):
    profile = get_profile()

    if not profile:
        return redirect('index')

    if request.method == 'GET':
        form = BookCreateForm()
    else:
        form = BookCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'books/add-book.html', context)


def edit_book(request, book_id):
    profile = get_profile()

    if not profile:
        return redirect('index')

    book = Book.objects.filter(pk=book_id).get()

    if request.method == 'GET':
        form = BookEditForm(instance=book)
    else:
        form = BookEditForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'book_id': book_id,
        'profile': profile,
    }

    return render(request, 'books/edit-book.html', context)


def details_book(request, book_id):
    profile = get_profile()

    if not profile:
        return redirect('index')

    book = Book.objects.filter(pk=book_id).get()

    context = {
        'book': book,
        'profile': profile,
    }

    return render(request, 'books/book-details.html', context)


def delete_book(request, book_id):
    profile = get_profile()

    if not profile:
        return redirect('index')

    book = Book.objects.filter(pk=book_id).get()

    book.delete()

    return redirect('index')
