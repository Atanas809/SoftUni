from django.urls import path

from prep_exam02.profiles.views import add_profile, details_profile, delete_profile, edit_profile

urlpatterns = [
    path('create/', add_profile, name='add profile'),
    path('details/', details_profile, name='details profile'),
    path('delete/', delete_profile, name='delete profile'),
    path('edit/', edit_profile, name='edit profile'),
]
