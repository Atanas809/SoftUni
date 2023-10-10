from django.urls import path

from forms_demo_part2.web.views import index, show_animals

urlpatterns = [
    path('', index, name='index'),
    path('show/animals/', show_animals, name='show animals'),
]
