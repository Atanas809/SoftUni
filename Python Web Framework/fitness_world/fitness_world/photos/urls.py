from django.urls import path
from fitness_world.photos import views

urlpatterns = [
    path('create/', views.CreatePhotoView.as_view(), name='create photo'),
    path('details/<int:pk>/', views.DetailsPhotoView.as_view(), name='details photo'),
    path('edit/<int:pk>/', views.EditPhotoView.as_view(), name='edit photo'),
    path('delete/<int:pk>/', views.delete_photo, name='delete photo'),
]
