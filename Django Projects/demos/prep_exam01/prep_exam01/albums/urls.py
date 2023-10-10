from django.urls import path

from prep_exam01.albums.views import add_album, EditAlbum, details_album, DeleteAlbum

urlpatterns = [
    path('add/', add_album, name='add album'),
    path('edit/<int:id>/', EditAlbum.as_view(), name='edit album'),
    path('details/<int:id>/', details_album, name='details album'),
    path('delete/<int:id>/', DeleteAlbum.as_view(), name='delete album'),
]
