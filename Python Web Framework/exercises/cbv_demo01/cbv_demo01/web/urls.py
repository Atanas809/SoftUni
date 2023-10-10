from django.urls import path
from cbv_demo01.web import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('index/view/', views.IndexView.as_view(), name='base view'),
    path('index/template/view/', views.IndexTemplateView.as_view(), name='template view'),
    path('index/list/view/', views.IndexListView.as_view(), name='list view'),
    path('redirect/view/', RedirectView.as_view(url='/'), name='redirect view'),
    path('details/<int:pk>/', views.IndexDetailsView.as_view(), name='details view'),
    path('create/', views.EmployeeCreateView.as_view(), name='create view'),
    path('edit/<int:pk>/', views.EmployeeUpdateView.as_view(), name='edit view'),
    path('delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='delete view'),
]
