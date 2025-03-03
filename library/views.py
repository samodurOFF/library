from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response

from library.models import Book
from library.serializers import BookListSerializer, BookDetailSerializer, BookCreateSerializer
from rest_framework.pagination import PageNumberPagination

class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    pagination_class = PageNumberPagination
    page_size = 5

    def create(self, request, *args, **kwargs):
        data = request.data.copy() #dict obj
        if not data.get('author'):
            data['author'] = 1
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_page_size(self, request):
        page_size = request.query_params.get('page_size')
        if page_size and page_size.isdigit():
            return int(page_size)
        return self.page_size

    def get_queryset(self):
        page_size = self.get_page_size(self.request)
        self.pagination_class.page_size = page_size
        year = self.request.query_params.get('year')
        queryset = super().get_queryset()
        if year:
            queryset = queryset.filter(publish_date__year=year)

        return queryset.order_by('pk')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookCreateSerializer
        elif self.request.method == 'GET':
            return BookListSerializer

class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer


