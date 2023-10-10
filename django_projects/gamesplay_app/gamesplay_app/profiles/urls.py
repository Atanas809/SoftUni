from django.urls import path

from gamesplay_app.profiles.views import create_profile, edit_profile, details_profile, delete_profile

urlpatterns = [
    path('create/', create_profile, name='create profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('details/', details_profile, name='details profile'),
    path('delete/', delete_profile, name='delete profile'),
]
