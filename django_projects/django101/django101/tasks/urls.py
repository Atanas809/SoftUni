from django.urls import path
from django101.tasks.views import home, default_page

urlpatterns = (
    path('tasks/', home),
    path('', default_page)
)
