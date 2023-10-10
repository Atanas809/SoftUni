from django.urls import path, include

from my_music_app.albums.views import add_album, details_album, delete_album, edit_album

urlpatterns = [
    path('add/', add_album, name='add album'),
    path('details/<int:album_id>/', details_album, name='details_album'),
    path('edit/<int:album_id>/', edit_album, name='edit_album'),
    path('delete/<int:album_id>/', delete_album, name='delete_album'),
]
