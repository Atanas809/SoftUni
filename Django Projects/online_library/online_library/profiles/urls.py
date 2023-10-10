from django.urls import path, include

from online_library.profiles.views import details_profile, edit_profile, delete_profile

urlpatterns = [
    path('profile/', include([
        path('', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ]))
]
