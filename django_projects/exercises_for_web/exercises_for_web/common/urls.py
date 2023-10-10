from django.urls import path, include
from exercises_for_web.common import views

urlpatterns = [
    path('', views.index, name='home page'),
    path('like/button/<int:photo_id>/', views.like_button, name='like photo'),
    path('share/button/<int:photo_id>/', views.share_button, name='share photo'),
    path('comment/photo/<int:photo_id>/', views.comment_photo, name='comment photo'),
]
