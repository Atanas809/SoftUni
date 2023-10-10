from django.urls import path, include
from fitness_world.profiles import views

urlpatterns = [
    path('login/', views.SignInView.as_view(), name='sign in'),
    path('register/', views.SignUpView.as_view(), name='sign up'),
    path('logout/', views.SignOutView.as_view(), name='sign out'),
    path('profile/', include([
        path('details/<int:pk>/', views.DetailsUserView.as_view(), name='details user'),
        path('edit/<int:pk>/', views.EditUserView.as_view(), name='edit user'),
        path('delete/<int:pk>/', views.DeleteUserView.as_view(), name='delete user'),
    ]))
]
