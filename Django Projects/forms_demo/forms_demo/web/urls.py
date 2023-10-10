from django.urls import path, include

from forms_demo.web.views import index_form, index_model_form

urlpatterns = [
    path('', index_form, name='index_form'),
    path('model/forms/', index_model_form, name='index_model_form'),
]
