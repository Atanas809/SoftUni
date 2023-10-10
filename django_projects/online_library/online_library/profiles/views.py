from django.shortcuts import render, redirect

from online_library.core.get_user_profile import get_profile
from online_library.profiles.forms import ProfileEditForm, ProfileDeleteForm


# Create your views here.

def details_profile(request):
    profile = get_profile()

    if not profile:
        return redirect('index')

    context = {
        'profile': profile,
    }

    return render(request, 'profiles/profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if not profile:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()

    if not profile:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/delete-profile.html', context)
