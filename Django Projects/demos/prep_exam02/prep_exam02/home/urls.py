from django.urls import path

from prep_exam02.home.views import home_page, dashboard

urlpatterns = [
    path('', home_page, name='home page'),
    path('dashboard/', dashboard, name='dashboard'),
]
