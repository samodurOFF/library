from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from library.models import Book
from library.serializers import BookListSerializer, BookDetailSerializer, BookCreateSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import GenericAPIView


class BookListView(GenericAPIView):
    queryset = Book.objects.all()
    pagination_class = PageNumberPagination
    pagination_class.page_size = 5
    page_size = 5

    def get(self, request, *args, **kwargs):
        year = request.query_params.get('year')
        page_size = self.get_page_size(request)
        self.page_size = page_size

        if year:
            self.queryset = Book.objects.filter(publish_date__year=year)

        results = self.paginate_queryset(self.get_queryset())
        serializer = self.get_serializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def get_page_size(self, request):
        page_size = request.query_params.get('page_size')
        if page_size and page_size.isdigit():
            return int(page_size)
        return self.page_size  # Использование значения по умолчанию

    def post(self, request):
        serializer = BookCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return BookDetailSerializer
        elif self.request.method == 'POST':
            return BookCreateSerializer


class BookDetailView(APIView):

    def get_book(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None

    def get(self, request, pk):
        book = self.get_book(pk)
        if book is None:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookDetailSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        book = self.get_book(pk)
        if book is None:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookDetailSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):

        book = self.get_book(pk)
        if book is None:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookDetailSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_book(pk)
        if book is None:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        book.delete()
        return Response({'message': 'Book was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
