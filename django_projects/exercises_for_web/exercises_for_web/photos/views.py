from django.shortcuts import render, redirect

from exercises_for_web.common.forms import CommentCreateForm
from exercises_for_web.core.photo_utils import likes_counter, user_liked_photo
from exercises_for_web.photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from exercises_for_web.photos.models import Photo


# Create your views here.


def add_photo(request):
    if request.method == "GET":
        form = PhotoCreateForm()

    else:
        form = PhotoCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)


def details_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo = likes_counter(photo)
    photo = user_liked_photo(photo)
    comments = photo.photocomment_set.all()
    comment_form = CommentCreateForm()

    context = {
        'photo': photo,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = PhotoEditForm(instance=photo)
    else:
        form = PhotoEditForm(request.POST, instance=photo)

        if form.is_valid():
            form.save()
            return redirect('details photo', pk=pk)

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = PhotoDeleteForm(instance=photo)
    else:
        form = PhotoDeleteForm(request.POST, instance=photo)

        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, 'photos/photo-delete-page.html', context)
