from django.urls import path, include
from django102.departments import views


urlpatterns = [
    path('', views.default_page),
    path('<str:page_name>/<int:page_id>/', views.search_page_by_name),
    path('<int:page_id>/', views.search_page_by_id, name='by-id'),
    path('all-pages/', views.valid_pages),
    path('<str:page_name>/', views.go_to_page, name='go-to-page'),
    path('all-pages/', include([
        path('<str:page>/', views.search_by_page)
    ])),
]