from django.shortcuts import render, redirect

from petstagram.common.forms import CommentCreateForm
from petstagram.core.decorators import is_owner
from petstagram.core.photo_utils import likes_count, user_liked_photo
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.utils import get_pet_by_slug_username


# views for pets page


def details_pet(request, username, pet_slug):
    pet = get_pet_by_slug_username(pet_slug, username)
    photos = [likes_count(photo) for photo in pet.photo_set.all()]
    photos = [user_liked_photo(photo) for photo in photos]
    comment_form = CommentCreateForm()

    context = {
        'pet': pet,
        'photos_count': pet.photo_set.count(),
        'photos': photos,
        'comment_form': comment_form,
        'is_owner': request.user == pet.user
    }
    return render(request, 'pets/pet-details-page.html', context)


def add_pet(request):
    if request.method == "GET":
        form = PetCreateForm()
    else:
        form = PetCreateForm(request.POST)

        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()

            return redirect('details user', pk=request.user.pk)

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-add-page.html', context)


def edit_pet(request, username, pet_slug):
    pet = get_pet_by_slug_username(pet_slug, username)

    if not is_owner(request, pet):
        return redirect('home page')

    if request.method == "GET":
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)

        if form.is_valid():
            form.save()
            return redirect('details pet', username=username, pet_slug=pet_slug)

    context = {
        'form': form,
        'username': username,
        'pet_slug': pet_slug,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, username, pet_slug):
    pet = get_pet_by_slug_username(pet_slug, username)

    if request.method == "GET":
        form = PetDeleteForm(instance=pet)
    else:
        form = PetDeleteForm(request.POST, instance=pet)

        if form.is_valid():
            form.save()
            return redirect('details user', pk=1)

    context = {
        'form': form,
        'username': username,
        'pet_slug': pet_slug,
    }

    return render(request, 'pets/pet-delete-page.html', context)
