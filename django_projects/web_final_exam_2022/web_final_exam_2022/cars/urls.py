from django.urls import path

from web_final_exam_2022.cars.views import create_car, edit_car, delete_car, details_car

urlpatterns = [
    path('create/', create_car, name='create car'),
    path('<int:car_id>/details/', details_car, name='details car'),
    path('<int:car_id>/edit/', edit_car, name='edit car'),
    path('<int:car_id>/delete/', delete_car, name='delete car'),
]
