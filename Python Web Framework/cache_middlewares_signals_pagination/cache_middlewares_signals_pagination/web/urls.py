from django.urls import path

from cache_middlewares_signals_pagination.web.views import index, show_session, raise_error

urlpatterns = [
    path('', index, name='index'),
    path('show_session/', show_session, name='show_session'),
    path('error/', raise_error, name='error'),
]


from .signals import *
