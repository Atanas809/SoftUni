from django.urls import path, include
from exercises_for_web.accounts import views

urlpatterns = [
    path('login/', views.login_user, name='login user'),
    path('register/', views.register_user, name='register user'),
    path('profile/<int:pk>/', include([
        path('', views.details_user, name='details user'),
        path('edit/', views.edit_user, name='edit user'),
        path('delete/', views.delete_user, name='delete user'),
    ]))
]
