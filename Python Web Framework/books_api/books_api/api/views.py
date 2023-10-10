from rest_framework.response import Response
from rest_framework import generics
from books_api.api.models import Book
from books_api.api.serializers import BookSerializer


class BookListApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = self.queryset

        book_id = self.request.query_params.get('book_id')

        if book_id:
            queryset = queryset.filter(pk=book_id)

        return queryset.all()


class BookDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
