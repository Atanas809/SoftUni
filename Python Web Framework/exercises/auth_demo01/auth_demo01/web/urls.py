from django.urls import path

from auth_demo01.web.views import index_with_no_permissions, index_with_login_required, index, create_user, view_permissions

urlpatterns = [
    path('', index, name='index'),
    path('without/', index_with_no_permissions, name='no permissions'),
    path('with/', index_with_login_required, name='with permissions'),
    path('create/', create_user, name='create'),
    path('permissions/<int:pk>/', view_permissions, name='perms'),
]
