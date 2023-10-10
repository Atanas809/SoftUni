from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('online_library.common.urls')),
    path('', include('online_library.profiles.urls')),
    path('', include('online_library.books.urls')),
]
