from django.shortcuts import render, redirect

from web_final_exam_2022.core.utils import get_user_profile, get_total_cars_prices
from web_final_exam_2022.profiles.forms import CreateUserForm, EditUserForm, DeleteUserForm


def add_user(request):
    if request.method == 'GET':
        form = CreateUserForm()

    else:
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    context = {
        'form': form,
    }

    return render(request, 'profiles/profile-create.html', context)


def details_user(request):
    user_profile = get_user_profile()
    total_sum_prices = get_total_cars_prices()

    context = {
        'user_profile': user_profile,
        'total_sum_prices': total_sum_prices,
    }

    return render(request, 'profiles/profile-details.html', context)


def edit_user(request):
    user_profile = get_user_profile()

    if request.method == 'GET':
        edit_form = EditUserForm(instance=user_profile)

    else:
        edit_form = EditUserForm(request.POST, instance=user_profile)

        if edit_form.is_valid():
            edit_form.save()
            return redirect('details user')

    context = {
        'edit_form': edit_form,
    }

    return render(request, 'profiles/profile-edit.html', context)


def delete_user(request):
    user_profile = get_user_profile()

    if request.method == 'GET':
        delete_form = DeleteUserForm(instance=user_profile)

    else:
        delete_form = DeleteUserForm(request.POST, instance=user_profile)

        if delete_form.is_valid():
            delete_form.save()
            return redirect('home page')

    context = {
        'delete_form': delete_form,
    }

    return render(request, 'profiles/profile-delete.html', context)
