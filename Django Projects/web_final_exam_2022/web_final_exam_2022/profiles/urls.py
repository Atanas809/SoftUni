from django.urls import path

from web_final_exam_2022.profiles.views import add_user, details_user, delete_user, edit_user

urlpatterns = [
    path('create/', add_user, name='add user'),
    path('details/', details_user, name='details user'),
    path('edit/', edit_user, name='edit user'),
    path('delete/', delete_user, name='delete user'),
]
