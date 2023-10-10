from django.urls import path
from django.views import generic as views
from cbv_introduction.web_cbv.views import IndexView, IndexViewWithTemplate, IndexViewWithListView, \
    IndexViewWithDetailsView, IndexViewWithCreateView, IndexViewWithUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('template/view/', IndexViewWithTemplate.as_view(), name='template view'),
    path('redirect/view/', views.RedirectView.as_view(url='/'), name='redirected'),
    path('home/', IndexViewWithListView.as_view(), name='list view'),
    path('details/student/<int:pk>/', IndexViewWithDetailsView.as_view(), name='details view'),
    path('create/student/', IndexViewWithCreateView.as_view(), name='create view'),
    path('edit/student/<int:pk>/', IndexViewWithUpdateView.as_view(), name='edit student'),
]
