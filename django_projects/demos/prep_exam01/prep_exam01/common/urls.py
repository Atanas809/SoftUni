from django.urls import path

from prep_exam01.common.views import index

urlpatterns = [
    path('', index, name='index'),
]
