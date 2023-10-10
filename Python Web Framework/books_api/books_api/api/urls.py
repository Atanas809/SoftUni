from django.urls import path

from books_api.api.views import BookListApiView, BookDetailApiView

urlpatterns = [
    path('books/', BookListApiView.as_view(), name='api list books'),
    path('books/<int:pk>/', BookDetailApiView.as_view(), name='api detail books'),
]
