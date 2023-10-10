from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_final_exam_2022.home.urls')),
    path('car/', include('web_final_exam_2022.cars.urls')),
    path('profile/', include('web_final_exam_2022.profiles.urls')),
]
