from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.models import User

from authentication_authorization.web.decorators import allowed_groups


# 'login required' with Function-base views
@login_required
def show_profile(request):
    return HttpResponse(f'Welcome back, {request.user.username.upper()}!')


# 'login required' with Class-base views
class ShowProfile(LoginRequiredMixin, generic.View):
    def get(self, request):
        return HttpResponse(f'Welcome back, {request.user.username.upper()}!')


# @allowed_groups(groups=['View/Change'])
@allowed_groups
def index(request):
    print(
        authenticate(username='atanas', password='admin'),
        authenticate(username='atanasss', password='admincho'),
    )
    logged_user = request.user.is_authenticated
    user_message = '' if logged_user else 'not '
    # new_user = User.objects.create_user(
    #     username='doncho',
    #     password='minkov',
    # )
    return HttpResponse(f'The user is {user_message}authenticated!')


def login_logout_users(request):
    print(request.user)
    current_user = User.objects.filter(pk=2).get()
    login(request, current_user)
    print(request.user)
    # logout(request)
    if request.user.is_authenticated:
        return HttpResponse('Logged in!')

    return HttpResponse('Logged out!')


def view_permissions(request):
    all_permissions = [
        'auth.add_user',
        'auth.change_user',
        'auth.delete_user',
        'auth.view_user',
    ]

    users = User.objects.all()

    for user in users:
        print('*' * 10)
        print(f"{user.username} ==> {user.has_perms(all_permissions)}")
        for permission in all_permissions:
            print(f"{permission}: {user.has_perm(permission)}")

    return HttpResponse('It work!')
