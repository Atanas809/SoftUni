from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    user = None

    if request.user.is_authenticated:
        user = request.user

    context = {
        'user': user,
    }

    return render(request, 'index.html', context)


def index_with_no_permissions(request):
    if not request.user.is_authenticated:
        return HttpResponse('This view is for anonymous users!')
    else:
        return redirect('with permissions')


@login_required
def index_with_login_required(request):
    logged_user = request.user
    return HttpResponse(f"Welcome back, {logged_user.username}!")


def create_user(request):
    new_user = {'username': 'Ivan', 'password': 'q1w2e3'}
    existing_user = User.objects.filter(username=new_user['username'])

    if existing_user:
        return HttpResponse('User already registered!')

    created_user = User.objects.create_user(username=new_user['username'], password=new_user['password'])
    login(request, created_user)
    return redirect('with permissions')
    # return HttpResponse(f"User {new_user['username']} created successfully!")


def view_permissions(request, pk):
    needed_user = User.objects.filter(pk=pk).get()

    all_perms = [
        'web.add_user',
        'web.change_user',
        'web.view_user',
        'web.delete_user',
    ]

    have_perms = needed_user.has_perms(all_perms)

    return HttpResponse(f"User {needed_user.username} ===> {have_perms}")

