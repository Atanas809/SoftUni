from django.urls import path

from prep_exam01.profiles.views import DeleteProfile, DetailsProfile, CreateProfile

urlpatterns = [
    path('details/', DetailsProfile.as_view(), name='details profile'),
    path('delete/', DeleteProfile.as_view(), name='delete profile'),
    path('create/', CreateProfile.as_view(), name='create profile'),
]
