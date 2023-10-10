from django.urls import path
from fitness_world.workouts import views

urlpatterns = [
    path('create/', views.CreateWorkoutView.as_view(), name='create workout'),
    path('edit/<str:username>/<slug:slug>/', views.EditWorkoutView.as_view(), name='edit workout'),
    path('details/<str:username>/<slug:slug>/', views.DetailsWorkoutView.as_view(), name='details workout'),
    path('delete/<str:username>/<slug:slug>/', views.delete_workout, name='delete workout'),
]
