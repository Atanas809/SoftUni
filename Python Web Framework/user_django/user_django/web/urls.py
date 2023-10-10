from django.urls import path

from user_django.web import views

urlpatterns = [
    path('', views.ShowUsers.as_view(), name='users list'),
]
