from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('demo003.web.urls')),
    path('', include('demo003.forms_web.urls')),
]
