from django.urls import path, include
from petstagram.accounts import views


urlpatterns = [
    path('register/', views.SignUpView.as_view(), name='register user'),
    path('login/', views.SignInView.as_view(), name='login user'),
    path('logout/', views.SingOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', views.DetailsUserView.as_view(), name='details user'),
        path('edit/', views.EditUserView.as_view(), name='edit user'),
        path('delete/', views.DeleteUserView.as_view(), name='delete user'),
    ])),
]
