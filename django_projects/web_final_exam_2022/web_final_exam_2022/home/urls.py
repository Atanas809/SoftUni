from django.urls import path

from web_final_exam_2022.home.views import home_page, catalogue_page

urlpatterns = [
    path('', home_page, name='home page'),
    path('catalogue/', catalogue_page, name='catalogue page'),
]
