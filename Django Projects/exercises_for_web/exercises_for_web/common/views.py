from django.shortcuts import render, redirect
from django.urls import reverse

from exercises_for_web.common.forms import CommentCreateForm, SearchForm
from exercises_for_web.common.models import PhotoLike
from exercises_for_web.core.photo_utils import likes_counter, user_liked_photo
from exercises_for_web.photos.models import Photo
from pyperclip import copy


# Create your views here.

def index(request):
    search_form = SearchForm(request.GET)
    search_pattern = None

    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['pet_name']

    all_photos = Photo.objects.all()

    if search_pattern:
        all_photos = all_photos.filter(tagged_pets__name__icontains=search_pattern)

    all_photos = [likes_counter(photo) for photo in all_photos]
    all_photos = [user_liked_photo(photo) for photo in all_photos]
    comment_form = CommentCreateForm()

    context = {
        'photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,
    }

    return render(request, 'common/home-page.html', context)


def get_user_liked_photos(photo_id):
    photo = PhotoLike.objects.filter(photo_id=photo_id)

    return photo


def like_button(request, photo_id):
    liked_photo = get_user_liked_photos(photo_id)

    if liked_photo:
        liked_photo.delete()
    else:
        new_like = PhotoLike.objects.create(
            photo_id=photo_id,
        )

        new_like.save()

    return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")


def share_button(request, photo_id):
    copy(request.META['HTTP_HOST'] + reverse('details photo', kwargs={'pk': photo_id}))

    return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")


def comment_photo(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).get()

    form = CommentCreateForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.photo = photo
        comment.save()

    return redirect(request.META['HTTP_REFERER'])
