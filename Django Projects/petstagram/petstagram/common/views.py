import pyperclip
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse

from petstagram.common.forms import CommentCreateForm, SearchForm
from petstagram.common.models import PhotoLike
from petstagram.core.photo_utils import likes_count, user_liked_photo
from petstagram.photos.models import Photo
from petstagram.common import utils


@login_required
def index(request):
    search_form = SearchForm(request.GET)
    search_pattern = None

    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['pet_name']

    photos = Photo.objects.all()

    if search_pattern:
        photos = photos.filter(tagged_pets__name__icontains=search_pattern)

    photos = [likes_count(photo) for photo in photos]
    photos = [user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
        'comment_form': CommentCreateForm(),
        'search_form': search_form,
    }

    return render(request, 'common/home-page.html', context)


@login_required
def like_photo(request, photo_id):
    liked_photo = PhotoLike.objects.filter(photo_id=photo_id, user_id=request.user.pk)

    if liked_photo:
        liked_photo.delete()
    else:
        PhotoLike.objects.create(
            photo_id=photo_id,
            user_id=request.user.pk,
        )

    redirect_path = utils.get_photo_url(request, photo_id)

    return redirect(redirect_path)


@login_required
def share_photo(request, photo_id):
    # photo_details_url = request.META['HTTP_REFERER'] + reverse('details photo', kwargs={'pk': photo_id})
    # http://127.0.0.1:8000//photos/1/

    photo_details_url = request.META['HTTP_HOST'] + reverse('details photo', kwargs={'pk': photo_id})
    # 127.0.0.1:8000/photos/1/

    # photo_details_url = request.META['HTTP_HOST'] + resolve_url('details photo', photo_id)
    # 127.0.0.1:8000/photos/1/

    pyperclip.copy(photo_details_url)

    return redirect(utils.get_photo_url(request, photo_id))


@login_required
def comment_photo(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).get()

    form = CommentCreateForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.photo = photo
        comment.save()

    return redirect(request.META['HTTP_REFERER'])
