from django.urls import path
from user_django.auth_app import views

urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    # path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-in/', views.SignInView.as_view(), name='sign-in'),
    path('sign-out/', views.SignOutView.as_view(), name='sign-out'),
    path('delete/user/<int:pk>/', views.DeleteProfile.as_view(), name='delete'),
]
