from django.urls import path
from models_demos.web import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/data/<int:pk>/', views.delete_data, name='delete data'),
    path('details/page/<int:pk>/<slug:slug>', views.department_details, name='department details'),
]
