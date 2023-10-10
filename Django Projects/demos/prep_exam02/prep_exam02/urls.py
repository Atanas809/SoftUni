from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('prep_exam02.home.urls')),
    path('profile/', include('prep_exam02.profiles.urls')),
    path('game/', include('prep_exam02.games.urls')),
]
