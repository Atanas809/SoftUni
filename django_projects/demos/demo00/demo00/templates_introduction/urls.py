from django.urls import path
from demo00.templates_introduction import views

urlpatterns = [
    path('', views.default_page, name='Home page'),
    path('dtl/variables/', views.dtl_variables, name='variables'),
    path('dtl/filters/', views.dtl_filters, name='some filters'),
    path('custom/filters/', views.custom_filters, name='custom filter'),
    path('custom/tags/', views.custom_tags, name='custom tags'),
    path('models/test/', views.show_all_departments, name='show departments'),
    path('delete/model/<int:pk>', views.delete_obj, name='delete'),
    path('details/page/<int:pk>/', views.absolute_url, name='details page'),
]
