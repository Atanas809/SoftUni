from django.shortcuts import render, redirect

from exercises_for_web.common.forms import CommentCreateForm
from exercises_for_web.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from exercises_for_web.pets.models import Pet


# Create your views here.


def add_pet(request):
    if request.method == "GET":
        form = PetCreateForm()
    else:
        form = PetCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('details user', pk=1)

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-add-page.html', context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()

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


def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    pet_photos_tagged = pet.photo_set.all()
    total_pet_photos = pet_photos_tagged.count()
    comment_form = CommentCreateForm()

    context = {
        'pet': pet,
        'pet_photos_tagged': pet_photos_tagged,
        'total_pet_photos': total_pet_photos,
        'comment_form': comment_form,
    }
    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()

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
