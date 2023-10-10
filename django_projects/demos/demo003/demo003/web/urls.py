from django.urls import path

from demo003.web.views import student_form, student_model_form, edit

urlpatterns = [
    path('', student_form, name='student form'),
    path('model/forms', student_model_form, name='student_model_form'),
    path('edit/page/<str:name>/', edit, name='edit'),
]
