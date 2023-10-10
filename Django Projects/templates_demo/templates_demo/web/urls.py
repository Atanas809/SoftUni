from django.urls import path
from templates_demo.web import views

urlpatterns = [
    path('', views.index, name='index'),
    path('go-to-home/', views.redirection, name='redirect to home'),
    path('about/', views.about, name='about'),
]
