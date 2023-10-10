from django.urls import path

from notes_app.common.views import index

urlpatterns = [
    path('', index, name='index'),
]
