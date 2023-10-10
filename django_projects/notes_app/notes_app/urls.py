from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes_app.common.urls')),
    path('', include('notes_app.notes.urls')),
    path('', include('notes_app.profiles.urls')),
]
