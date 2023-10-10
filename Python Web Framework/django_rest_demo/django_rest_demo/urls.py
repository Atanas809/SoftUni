from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('django_rest_demo.web.urls')),
    # Enables browsable API
    path('api-auth/', include('rest_framework.urls')),
]
