from django.shortcuts import render, redirect

from petstagram.common.forms import CommentCreateForm
from petstagram.core.photo_utils import likes_count, user_liked_photo
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from petstagram.photos.models import Photo


# views for photos page
def details_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photos_likes = [likes_count(photo)]
    liked_by_user = [user_liked_photo(photo)]
    comment_form = CommentCreateForm()

    context = {
        'photo': photo,
        'photo_likes': photos_likes,
        'liked_by_user': liked_by_user,
        'comment_form': comment_form,
    }

    return render(request, 'photos/photo-details-page.html', context)


def add_photo(request):
    if request.method == "GET":
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            form.save_m2m()

            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)


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