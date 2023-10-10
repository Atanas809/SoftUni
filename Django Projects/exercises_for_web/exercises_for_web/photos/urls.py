from django.urls import path, include
from exercises_for_web.photos import views


urlpatterns = [
    path('add/', views.add_photo, name='add photo'),
    path('<int:pk>/', include([
        path('', views.details_photo, name='details photo'),
        path('edit/', views.edit_photo, name='edit photo'),
        path('delete/', views.delete_photo, name='delete photo'),
    ]))
]
