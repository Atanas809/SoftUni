from django.urls import path

from notes_app.profiles.views import details_profile

urlpatterns = [
    path('profile/', details_profile, name='details profile'),
]
