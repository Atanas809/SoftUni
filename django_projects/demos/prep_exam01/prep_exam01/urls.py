from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('prep_exam01.common.urls')),
    path('album/', include('prep_exam01.albums.urls')),
    path('profile/', include('prep_exam01.profiles.urls')),
]
