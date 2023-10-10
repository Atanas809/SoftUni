from django.urls import path

from gamesplay_app.games.views import create_game, edit_game, details_game, delete_game

urlpatterns = [
    path('create/', create_game, name='create game'),
    path('edit/<int:game_id>/', edit_game, name='edit game'),
    path('details/<int:game_id>/', details_game, name='details game'),
    path('delete/<int:game_id>/', delete_game, name='delete game'),
]
