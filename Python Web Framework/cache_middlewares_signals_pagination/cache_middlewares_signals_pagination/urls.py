from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cache_middlewares_signals_pagination.web.urls')),
]
