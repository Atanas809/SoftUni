from django.urls import path
from fitness_world.common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('like/<int:pk>/', views.like_photo, name='like photo'),
    path('create/comment/<int:pk>/', views.create_comment, name='comment photo'),
    path('edit/comment/<int:pk>/', views.EditCommentView.as_view(), name='edit comment'),
    path('delete/comment/<int:pk>/', views.delete_comment, name='delete comment'),
    path('share/photo/<int:pk>/', views.share_photo, name='share photo'),
]
