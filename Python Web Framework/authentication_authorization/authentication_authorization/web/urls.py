from django.urls import path

from authentication_authorization.web.views import index, \
    login_logout_users, view_permissions, show_profile, ShowProfile

urlpatterns = [
    path('', index, name='index'),
    path('login/logout/', login_logout_users, name='login logout'),
    path('permissions/', view_permissions, name='permissions'),
    path('profile/1/', show_profile, name='profile 1'),
    path('profile/2/', ShowProfile.as_view(), name='profile 2'),
]
