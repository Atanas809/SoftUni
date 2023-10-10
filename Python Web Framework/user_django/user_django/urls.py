from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user_django.auth_app.urls')),
    path('', include('user_django.web.urls')),
]
