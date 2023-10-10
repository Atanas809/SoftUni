from django.urls import path

from prep_exam02.games.views import add_game, details_game, delete_game, edit_game

urlpatterns = [
    path('create/', add_game, name='add game'),
    path('details/<int:id>/', details_game, name='details game'),
    path('delete/<int:id>/', delete_game, name='delete game'),
    path('edit/<int:id>/', edit_game, name='edit game'),
]
