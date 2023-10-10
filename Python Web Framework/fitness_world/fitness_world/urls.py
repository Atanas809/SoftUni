from django.conf.urls.static import static

from fitness_world import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fitness_world.common.urls')),
    path('photo/', include('fitness_world.photos.urls')),
    path('', include('fitness_world.profiles.urls')),
    path('workout/', include('fitness_world.workouts.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
