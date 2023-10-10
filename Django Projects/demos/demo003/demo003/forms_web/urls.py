from django.urls import path

from demo003.forms_web.views import index, register_form, register_model_form, update_course

urlpatterns = [
    path('', index, name='index'),
    path('register/user/', register_form, name='register user'),
    path('register/user/model/form', register_model_form, name='model form'),
    path('edit/course/<slug:slug>/', update_course, name='update course'),
]
