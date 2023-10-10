from django.urls import path, include
from petstagram.common import views

urlpatterns = [
    path('', views.index, name='home page'),
    path('like/<int:photo_id>/', views.like_photo, name='like photo'),
    path('share/<int:photo_id>/', views.share_photo, name='share photo'),
    path('comment/<int:photo_id>/', views.comment_photo, name='comment photo'),
]
