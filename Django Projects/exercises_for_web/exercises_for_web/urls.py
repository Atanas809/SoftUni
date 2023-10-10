from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exercises_for_web.common.urls')),
    path('accounts/', include('exercises_for_web.accounts.urls')),
    path('photos/', include('exercises_for_web.photos.urls')),
    path('pets/', include('exercises_for_web.pets.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
