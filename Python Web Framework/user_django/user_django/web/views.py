from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic as views

# from user_django.auth_app.models import AppUser

UserModel = get_user_model()


class ShowUsers(LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'web/index.html'
    context_object_name = 'users'

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #
    #     context['has_first_name'] = AppUser.has_first_name(self.request.user)
    #
    #     return context
