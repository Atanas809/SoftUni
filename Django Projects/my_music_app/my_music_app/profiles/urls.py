from django.urls import path, include

from my_music_app.profiles.views import details_profile, delete_profile

urlpatterns = [
    path('details/', details_profile, name='details profile'),
    path('delete/', delete_profile, name='delete_profile'),
]
